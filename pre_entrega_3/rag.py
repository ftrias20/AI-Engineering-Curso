from pathlib import Path
import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate

from schemas import RAGResponse


# Carpeta donde esta guardada la base vectorial
VECTORSTORE_PATH = Path(__file__).parent / "vectorstore"

# Carga el .env ubicado en la raiz del proyecto
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)


# Modelo que genera los embeddings
embeddings = OpenAIEmbeddings(
    model=os.getenv(
        "OPENAI_EMBEDDING_MODEL",
        "text-embedding-3-small"
    )
)


# Abre la base vectorial que ya fue creada en ingest.py
vectorstore = Chroma(
    collection_name="pre_entrega_3",
    embedding_function=embeddings,
    persist_directory=str(VECTORSTORE_PATH)
)


# Retriever que busca los 3 chunks mas relacionados
retriever = vectorstore.as_retriever(
    search_kwargs={
        "k": 3
    }
)


# Modelo que va a generar la respuesta final
model = ChatOpenAI(
    model=os.getenv(
        "OPENAI_MODEL",
        "gpt-4o-mini"
    ),
    temperature=0
)


# Parser que valida la respuesta usando RAGResponse
parser = PydanticOutputParser(
    pydantic_object=RAGResponse
)


# Prompt que obliga al modelo a usar solamente el contexto
prompt = ChatPromptTemplate.from_template(
    """
Sos un asistente tecnico.

Responde solamente utilizando la informacion
del CONTEXTO proporcionado.

Si la respuesta no se encuentra en el contexto,
responde exactamente "No lo se".

Las referencias deben contener solamente los nombres
de los archivos utilizados para responder.

CONTEXTO:
{contexto}

PREGUNTA:
{pregunta}

{format_instructions}
"""
).partial(
    format_instructions=parser.get_format_instructions()
)


# Pipeline LCEL:
# prompt -> modelo -> validacion Pydantic
chain = prompt | model | parser


async def get_rag_response(query: str) -> RAGResponse:

    # Busca los 3 fragmentos mas relacionados con la pregunta
    documentos = await retriever.ainvoke(query)

    # Arma un unico texto con los chunks recuperados
    contexto = "\n\n".join(
        [
            f"Archivo: {documento.metadata['source']}\n"
            f"{documento.page_content}"
            for documento in documentos
        ]
    )

    # Envia la pregunta y el contexto al pipeline
    respuesta = await chain.ainvoke(
        {
            "contexto": contexto,
            "pregunta": query
        }
    )

    return respuesta
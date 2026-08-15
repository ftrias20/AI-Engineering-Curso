import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Carpeta donde estan los documentos
DATA_PATH = Path(__file__).parent / "data"

# Carga el .env ubicado en la raiz del proyecto
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)

# Nombre del indice creado en Pinecone
INDEX_NAME = os.getenv("INDEX_NAME")

# Namespace utilizado para separar estos documentos
NAMESPACE = "documentacion-tecnica"


def cargar_documentos():
    documentos = []

    # Busca todos los archivos markdown
    for archivo in DATA_PATH.glob("*.md"):

        # Lee todo el contenido del archivo
        contenido = archivo.read_text(
            encoding="utf-8"
        )

        # La categoria se obtiene del nombre del archivo
        categoria = archivo.stem

        documentos.append(
            Document(
                page_content=contenido,
                metadata={
                    "source": archivo.name,
                    "page": 1,
                    "category": categoria
                }
            )
        )

    return documentos


def dividir_documentos(documentos):

    # Divide los documentos en chunks de 600 tokens
    # y repite 50 tokens entre un chunk y el siguiente
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base",
        chunk_size=600,
        chunk_overlap=50
    )

    # Divide los documentos y mantiene la metadata
    chunks = splitter.split_documents(documentos)

    return chunks


def guardar_en_pinecone(chunks):

    # Modelo que convierte cada chunk en un vector
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    # Se conecta al indice de Pinecone que ya creamos
    vectorstore = PineconeVectorStore(
        index_name=INDEX_NAME,
        embedding=embeddings,
        namespace=NAMESPACE
    )

    # Crea un id para cada chunk
    # Esto evita duplicarlos si ejecutamos la ingesta otra vez
    ids = [
        f"{chunk.metadata['source']}-{indice}"
        for indice, chunk in enumerate(
            chunks,
            start=1
        )
    ]

    # Genera los embeddings y guarda los chunks en Pinecone
    vectorstore.add_documents(
        documents=chunks,
        ids=ids
    )

    print(
        f"Se guardaron {len(chunks)} chunks en Pinecone."
    )


if __name__ == "__main__":

    # Lee los archivos de la carpeta data
    documentos = cargar_documentos()

    print(
        f"Documentos encontrados: {len(documentos)}"
    )

    # Divide los documentos en chunks
    chunks = dividir_documentos(documentos)

    print(
        f"Chunks generados: {len(chunks)}"
    )

    # Muestra informacion de cada chunk
    for indice, chunk in enumerate(
        chunks,
        start=1
    ):
        print(
            f"{indice}. "
            f"{chunk.metadata['source']} | "
            f"categoria: {chunk.metadata['category']} | "
            f"{len(chunk.page_content)} caracteres"
        )

    # Sube los chunks al indice de Pinecone
    guardar_en_pinecone(chunks)
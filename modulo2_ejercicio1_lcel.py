import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Cargo las variables guardadas en el archivo .env
load_dotenv()


# Defino el prompt con los roles System y Human
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Sos un asistente experto en AI Engineering. "
        "Responde de forma clara y sencilla."
    ),
    (
        "human",
        "{pregunta}"
    )
])


# Configuro el modelo que va a responder
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


# Extraigo solo el texto de la respuesta del modelo
parser = StrOutputParser()


# Armo una cadena LCEL de LangChain
# recibe la pregunta, construye el prompt, consulta el modelo
# y devuelve solamente el texto de la respuesta
chain = prompt | model | parser


async def main():
    # Ejecuto toda la cadena de forma asincrona
    resultado = await chain.ainvoke({
        "pregunta": "Que es un LLM? Explicalo en pocas palabras."
    })

    # El parser hace que resultado sea un texto simple
    print(resultado)


if __name__ == "__main__":
    # Creo el event loop y ejecuto la funcion principal
    asyncio.run(main())
import logging

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from schemas import TechnicalExtraction


load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Obtiene el modelo configurado en el archivo .env
model_name = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o-mini"
)

# Las variables del .env se leen como texto,
# por eso convertimos la temperatura a float
temperature = float(
    os.getenv("LLM_TEMPERATURE", "0")
)

# Configura el modelo de OpenAI mediante LangChain
model = ChatOpenAI(
    model=model_name,
    temperature=temperature
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Analiza el texto y extrae las tecnologias utilizadas, "
        "el nivel de criticidad y un resumen tecnico breve."
    ),
    (
        "human",
        "{texto}"
    )
])
structured_model = model.with_structured_output(
    TechnicalExtraction
)
chain = prompt | structured_model

resilient_chain = chain.with_retry(
    stop_after_attempt=3,
    wait_exponential_jitter=True
)
async def process_text(text: str) -> TechnicalExtraction:
    
    logging.info("Iniciando procesamiento del texto")

  
    logging.info("La cadena dispone de hasta 3 intentos")

    try:
        # Ejecuta de forma asincrona toda la cadena:
        # prompt -> modelo -> validacion con Pydantic
        result = await resilient_chain.ainvoke(
            {
                # Este valor reemplaza {texto} dentro del prompt
                "texto": text
            }
        )

        # Si llegamos hasta aca, el resultado fue validado correctamente
        logging.info(
            "Texto procesado y validado correctamente"
        )

        # Devuelve un objeto TechnicalExtraction
        return result

    except Exception as error:
        # Registra el error luego de que se agotaron los intentos
        logging.error(
            "No se pudo procesar el texto luego de los reintentos: "
            f"{error}"
        )

        # Vuelve a lanzar el error para que main.py pueda manejarlo
        raise
import os
from pathlib import Path

from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec


# Carga el .env ubicado en la raiz del proyecto
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)

# Obtiene las variables de configuracion
api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("INDEX_NAME")

# Crea el cliente de Pinecone
pc = Pinecone(
    api_key=api_key
)

# Verifica si el indice ya existe
if index_name not in pc.list_indexes().names():

    print(
        f"El indice '{index_name}' no existe. "
        "Se va a crear."
    )

    # Crea un indice Serverless
    # Dimension 1536 porque usamos text-embedding-3-small
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

    print("Indice creado correctamente.")

else:
    print(
        f"El indice '{index_name}' ya existe."
    )


# Consulta la configuracion y estado del indice
index_info = pc.describe_index(
    name=index_name
)

print("\nEstado del indice:")
print(f"Nombre: {index_info.name}")
print(f"Dimension: {index_info.dimension}")
print(f"Metric: {index_info.metric}")
print(f"Ready: {index_info.status['ready']}")

print(f"\nIndice configurado: {index_name}")
print("Conexion con Pinecone creada correctamente")
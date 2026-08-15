from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Carpeta donde estan los documentos que vamos a procesar
DATA_PATH = Path(__file__).parent / "data"
# Carpeta donde ChromaDB va a guardar la base vectorial
VECTORSTORE_PATH = Path(__file__).parent / "vectorstore"

# Carga el .env que tenemos en la raiz del proyecto
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)

def cargar_documentos():
    documentos = []

    # Busca todos los archivos .txt dentro de la carpeta data
    for archivo in DATA_PATH.glob("*.txt"):

        # Lee todo el contenido del archivo
        contenido = archivo.read_text(
            encoding="utf-8"
        )

        documentos.append(
            {
                "archivo": archivo.name,
                "contenido": contenido
            }
        )

    return documentos


def dividir_documentos(documentos):
    chunks = []

    # Divide los textos en fragmentos de 500 tokens
    # y repite 50 tokens entre un fragmento y el siguiente
    splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        encoding_name="cl100k_base",
        chunk_size=500,
        chunk_overlap=50
    )

    for documento in documentos:

        # Divide el contenido completo del archivo
        fragmentos = splitter.split_text(
            documento["contenido"]
        )

        for fragmento in fragmentos:
            chunks.append(
    Document(
        # Guarda el texto real del fragmento
        page_content=fragmento,

        # Guarda de que archivo salio el fragmento
        metadata={
            "source": documento["archivo"]
        }
    )
)

    return chunks
def guardar_en_chroma(chunks):

    # Si la base ya existe y tiene contenido no la volvemos a crear
    if VECTORSTORE_PATH.exists() and any(VECTORSTORE_PATH.iterdir()):
        print("La base vectorial ya existe. No se vuelve a indexar.")
        return

    # Modelo que convierte cada chunk de texto en un vector
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    # Crea una base ChromaDB persistente en disco
    vectorstore = Chroma(
        collection_name="pre_entrega_3",
        embedding_function=embeddings,
        persist_directory=str(VECTORSTORE_PATH)
    )

    # Genera los embeddings y guarda los chunks en ChromaDB
    vectorstore.add_documents(chunks)

    print(
        f"Base vectorial creada con {len(chunks)} chunks."
    )

if __name__ == "__main__":
    documentos = cargar_documentos()

    print(f"Documentos encontrados: {len(documentos)}")

    chunks = dividir_documentos(documentos)

    print(f"Chunks generados: {len(chunks)}")

    for indice, chunk in enumerate(chunks, start=1):
        print(
            f"{indice}. {chunk.metadata['source']} - "
            f"{len(chunk.page_content)} caracteres"
        )

    guardar_en_chroma(chunks)
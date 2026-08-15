import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.retrievers import BM25Retriever
from langchain_classic.retrievers.ensemble import EnsembleRetriever

from ingest import cargar_documentos, dividir_documentos


# Carga el .env ubicado en la raiz del proyecto
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)

# Nombre del indice de Pinecone
INDEX_NAME = os.getenv("INDEX_NAME")

# Namespace utilizado durante la ingesta
NAMESPACE = "documentacion-tecnica"


class RAGSystem:

    def __init__(self):

        # Modelo de embeddings utilizado en Pinecone
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )

        # Conexion con Pinecone
        vectorstore = PineconeVectorStore(
            index_name=INDEX_NAME,
            embedding=embeddings,
            namespace=NAMESPACE
        )

        # Retriever semantico de Pinecone
        pinecone_retriever = vectorstore.as_retriever(
            search_kwargs={
                "k": 5
            }
        )

        # Carga los documentos locales para BM25
        documentos = cargar_documentos()

        # Divide los documentos igual que en la ingesta
        chunks = dividir_documentos(documentos)

        # Retriever lexical BM25
        bm25_retriever = BM25Retriever.from_documents(
            chunks
        )

        bm25_retriever.k = 5

        # Combina busqueda semantica y lexical
        self.retriever = EnsembleRetriever(
            retrievers=[
                pinecone_retriever,
                bm25_retriever
            ],
            weights=[
                0.5,
                0.5
            ]
        )

    def buscar(self, query: str):

        # Devuelve los documentos recuperados
        resultados = self.retriever.invoke(
            query
        )

        return resultados[:5]


if __name__ == "__main__":

    rag = RAGSystem()

    pregunta = "Que es un patron Singleton?"

    resultados = rag.buscar(
        pregunta
    )

    print(f"Pregunta: {pregunta}")

    for indice, documento in enumerate(
        resultados,
        start=1
    ):
        print(f"\n--- Resultado {indice} ---")

        print(
            f"Archivo: {documento.metadata['source']}"
        )

        print(
            f"Categoria: {documento.metadata['category']}"
        )

        print(
            documento.page_content
        )
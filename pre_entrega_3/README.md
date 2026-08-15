# Pre-entrega 3 - Sistema RAG local

Sistema de recuperacion semantica que utiliza documentos locales como fuente de informacion.

El flujo implementado es:

Documentos -> Chunking -> Embeddings -> ChromaDB -> Retriever -> LLM -> Respuesta validada

## Estructura

- `data/`: documentos utilizados como fuente de conocimiento.
- `ingest.py`: carga los documentos, genera los chunks y los guarda en ChromaDB.
- `rag.py`: realiza la busqueda semantica y genera la respuesta utilizando LangChain.
- `schemas.py`: contiene el modelo Pydantic utilizado para validar la respuesta.
- `main.py`: ejecuta una pregunta valida y una pregunta trampa.
- `.env.example`: variables de entorno necesarias.

## Instalacion

Crear y activar un entorno virtual e instalar las dependencias:

```bash
pip install -r pre_entrega_3/requirements.txt
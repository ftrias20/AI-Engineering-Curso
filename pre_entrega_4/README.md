# Pre-entrega 4 - Sistema RAG con Pinecone

## Descripcion

Este proyecto implementa un sistema de recuperacion hibrida utilizando Pinecone y BM25.

La busqueda combina:

- Pinecone para busqueda semantica mediante embeddings.
- BM25 para busqueda lexical basada en palabras.
- EnsembleRetriever para combinar ambos resultados.

Tambien se incluye una evaluacion utilizando Precision@5 y Recall@5 sobre un Golden Set de preguntas conocidas.


## Estructura

```text
pre_entrega_4/
├── data/
│   ├── arquitectura.md
│   ├── metodologias_agiles.md
│   └── patrones.md
├── setup_pinecone.py
├── ingest.py
├── rag_system.py
├── evaluate.py
├── golden_set.json
├── requirements.txt
├── .env.example
└── README.md
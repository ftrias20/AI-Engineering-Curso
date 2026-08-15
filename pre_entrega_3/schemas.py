from pydantic import BaseModel, Field


class RAGResponse(BaseModel):
    # Respuesta generada usando solamente el contexto recuperado
    respuesta: str = Field(min_length=1)

    # Archivos utilizados como fuente para generar la respuesta
    referencias: list[str]
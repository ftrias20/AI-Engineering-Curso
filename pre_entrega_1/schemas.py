from typing import Literal

from pydantic import BaseModel, Field
from typing import Literal, Optional

class ChatMessage(BaseModel):
    # El rol solo puede tener uno de estos valores
    role: Literal["system", "user", "assistant"]

    # El mensaje debe contener al menos un caracter
    content: str = Field(min_length=1)


class LLMConfig(BaseModel):
    # Proveedor que se va a utilizar
    provider: Literal["openai", "anthropic"]

    # Nombre del modelo a utilizar
    model: str = Field(min_length=1)

    # Controla la variacion de las respuestas
    # Solo acepta valores entre 0 y 2
    temperature: float = Field(default=0, ge=0, le=2)

    # Cantidad maxima de tokens que puede generar la respuesta
    max_tokens: int = Field(default=500, gt=0)

class ModelResponse(BaseModel):
    # Indica si la llamada termino correctamente
    success: bool

    # Contiene la respuesta del modelo cuando la llamada fue exitosa
    content: Optional[str] = None

    # Indica que proveedor atendio la solicitud
    provider: Literal["openai", "anthropic"]

    # Contiene el detalle cuando ocurre un error controlado
    error: Optional[str] = None
   








if __name__ == "__main__":
    mensaje = ChatMessage(
        role="user",
        content="Que es la entropia?"
    )

    config = LLMConfig(
        provider="openai",
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=300
    )



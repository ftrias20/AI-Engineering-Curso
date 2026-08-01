from abc import ABC, abstractmethod
from collections.abc import AsyncIterator

from schemas import ChatMessage, LLMConfig, ModelResponse


class BaseLLMClient(ABC):
    def __init__(self, config: LLMConfig):
        # Todos los proveedores reciben la misma configuracion
        self.config = config

    @abstractmethod
    async def generate(
        self,
        messages: list[ChatMessage]
    ) -> ModelResponse:
        # Cada proveedor debe implementar su propia llamada a la API
        pass

    @abstractmethod
    async def stream(
        self,
        messages: list[ChatMessage]
    ) -> AsyncIterator[str]:
        # El yield indica que este metodo sera un generador asincrono
        yield ""
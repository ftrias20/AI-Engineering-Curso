import asyncio
from abc import ABC, abstractmethod
from enum import Enum
from pydantic import BaseModel, SecretStr
# TODO: Importa los clientes asíncronos de openai y anthropic

class Provider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"

class LLMConfig(BaseModel):
    """
    TODO: Define los campos para las API Keys usando SecretStr
    y una validación para asegurar que existan cuando se necesiten.
    """
    pass

class BaseLLMClient(ABC):
    @abstractmethod
    async def chat(self, prompt: str) -> str:
        pass

# TODO: Implementa OpenAIClient y AnthropicClient heredando de BaseLLMClient

class LLMFactory:
    @staticmethod
    def create_client(provider: Provider, config: LLMConfig) -> BaseLLMClient:
        # TODO: Implementa la lógica de selección de cliente
        pass

async def main():
    # TODO: Instancia la configuración y crea un cliente usando el Factory
    pass

if __name__ == "__main__":
    asyncio.run(main())

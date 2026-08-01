from base_client import BaseLLMClient
from schemas import LLMConfig
from openai_client import OpenAIClient
from anthropic_client import AnthropicClient


class AsyncLLMManager:
    @staticmethod
    def create_client(config: LLMConfig) -> BaseLLMClient:
        # Crea el cliente correspondiente segun el proveedor configurado
        if config.provider == "openai":
            return OpenAIClient(config)

        if config.provider == "anthropic":
            return AnthropicClient(config)

        # Validacion extra por seguridad
        raise ValueError(
            f"Proveedor no soportado: {config.provider}"
        )
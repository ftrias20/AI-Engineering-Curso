from collections.abc import AsyncIterator

from openai import AsyncOpenAI

from base_client import BaseLLMClient
from schemas import ChatMessage, LLMConfig, ModelResponse

class OpenAIClient(BaseLLMClient):
    def __init__(self, config: LLMConfig):
        super().__init__(config)

        # Cliente asincrono del SDK oficial de OpenAI
        self.client = AsyncOpenAI()

    async def generate(
        self,
        messages: list[ChatMessage]
    ) -> ModelResponse:
        try:
            # Convierto los modelos Pydantic en diccionarios
            formatted_messages = [
                message.model_dump()
                for message in messages
            ]

            # Realizo la llamada asincrona a OpenAI
            response = await self.client.chat.completions.create(
                model=self.config.model,
                messages=formatted_messages,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )

            # Obtengo el texto de la primera respuesta
            content = response.choices[0].message.content or ""

            return ModelResponse(
                success=True,
                content=content,
                provider="openai"
            )

        except Exception as error:
            # Devuelvo un error controlado para no romper el programa
            return ModelResponse(
                success=False,
                provider="openai",
                error=str(error)
            )

    async def stream(
        self,
        messages: list[ChatMessage]
    ) -> AsyncIterator[str]:
        try:
            formatted_messages = []

            for message in messages:
                message_dict = message.model_dump()
                formatted_messages.append(message_dict)

            response_stream = await self.client.chat.completions.create(
                model=self.config.model,
                messages=formatted_messages,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens,
                stream=True
            )

            async for chunk in response_stream:
                content = chunk.choices[0].delta.content

                if content:
                    yield content

        except Exception as error:
            yield f"Error controlado de OpenAI: {error}"
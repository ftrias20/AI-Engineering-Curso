from collections.abc import AsyncIterator

from anthropic import AsyncAnthropic

from base_client import BaseLLMClient
from schemas import ChatMessage, LLMConfig, ModelResponse


class AnthropicClient(BaseLLMClient):
    def __init__(self, config: LLMConfig):
        # Llama al constructor de la clase base
        # y guarda la configuracion en self.config
        super().__init__(config)

        # Cliente asincrono oficial de Anthropic
        self.client = AsyncAnthropic()


    async def generate(
        self,
        messages: list[ChatMessage]
    ) -> ModelResponse:
        try:
            system_prompt = ""
            formatted_messages = []

            for message in messages:
                if message.role == "system":
                    # Anthropic recibe el mensaje system por separado
                    system_prompt = message.content
                else:
                    # Los mensajes user y assistant van en la lista
                    formatted_messages.append(
                        {
                            "role": message.role,
                            "content": message.content
                        }
                    )

            response = await self.client.messages.create(
                model=self.config.model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                system=system_prompt,
                messages=formatted_messages
            )

            content = ""

            for block in response.content:
                if block.type == "text":
                    content += block.text

            return ModelResponse(
                success=True,
                content=content,
                provider="anthropic"
            )

        except Exception as error:
            return ModelResponse(
                success=False,
                provider="anthropic",
                error=str(error)
            )

    async def stream(
        self,
        messages: list[ChatMessage]
    ) -> AsyncIterator[str]:
        try:
            system_prompt = ""
            formatted_messages = []

            for message in messages:
                if message.role == "system":
                    system_prompt = message.content
                else:
                    formatted_messages.append(
                        {
                            "role": message.role,
                            "content": message.content
                        }
                    )

            async with self.client.messages.stream(
                model=self.config.model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                system=system_prompt,
                messages=formatted_messages
            ) as response_stream:

                async for text in response_stream.text_stream:
                    yield text

        except Exception as error:
            yield f"Error controlado de Anthropic: {error}"
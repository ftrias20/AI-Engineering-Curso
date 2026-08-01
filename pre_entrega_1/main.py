import asyncio
import os
from typing import Literal, cast

from dotenv import load_dotenv

from llm_manager import AsyncLLMManager
from schemas import ChatMessage, LLMConfig


async def main():
    # Carga las variables guardadas en el archivo .env
    load_dotenv()

    try:
        # Obtiene el proveedor configurado
        provider_value = os.getenv(
            "LLM_PROVIDER",
            "openai"
        ).strip().lower()

        # Valida que el proveedor sea compatible
        if provider_value not in ("openai", "anthropic"):
            print(f"Proveedor no soportado: {provider_value}")
            return

        provider = cast(
            Literal["openai", "anthropic"],
            provider_value
        )

        # Selecciona el modelo segun el proveedor
        if provider == "openai":
            model = os.getenv(
                "OPENAI_MODEL",
                "gpt-4o-mini"
            )

            provider_name = "OpenAI"

        else:
            model = os.getenv(
                "ANTHROPIC_MODEL",
                ""
            )

            provider_name = "Anthropic"

        # Valida que exista un modelo configurado
        if not model:
            print(
                f"No se configuro un modelo para {provider_name}"
            )
            return

        # Lee la configuracion general del modelo
        temperature = float(
            os.getenv("LLM_TEMPERATURE", "0")
        )

        max_tokens = int(
            os.getenv("LLM_MAX_TOKENS", "300")
        )

        # Pydantic valida los valores configurados
        config = LLMConfig(
            provider=provider,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens
        )

        messages = [
            ChatMessage(
                role="system",
                content="Responde de forma clara y sencilla."
            ),
            ChatMessage(
                role="user",
                content="Que es la entropia?"
            )
        ]

        # El manager crea OpenAIClient o AnthropicClient
        cliente = AsyncLLMManager.create_client(config)

        # Prueba de respuesta normal
        respuesta = await cliente.generate(messages)

        if respuesta.success:
            print(f"Respuesta normal de {provider_name}:")
            print(respuesta.content)
        else:
            print(f"Ocurrio un error en {provider_name}:")
            print(respuesta.error)

        # Prueba de respuesta en streaming
        print(f"\nRespuesta de {provider_name} en streaming:")

        async for fragmento in cliente.stream(messages):
            print(fragmento, end="", flush=True)

        print()

    except ValueError as error:
        # Captura valores invalidos del archivo .env
        print(f"Error de configuracion: {error}")

    except Exception as error:
        # Captura cualquier otro error inesperado
        print(f"Error controlado: {error}")


if __name__ == "__main__":
    asyncio.run(main())
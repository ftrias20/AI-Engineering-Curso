import asyncio
import json
from pathlib import Path

from langchain_core.messages import HumanMessage

from agent import crear_app


TRACE_PATH = Path(__file__).parent / "trace.json"


async def main():

    pregunta = (
        "El sistema muestra el error POS-204. "
        "Decime que significa y como tengo que resolverlo."
    )

    config = {
        "configurable": {
            "thread_id": "trace_demo_02"
        },
        "recursion_limit": 10
    }

    trace = [
        {
            "tipo": "usuario",
            "contenido": pregunta
        }
    ]

    async with crear_app() as app:

        async for update in app.astream(
            {
                "messages": [
                    HumanMessage(
                        content=pregunta
                    )
                ]
            },
            config=config,
            stream_mode="updates"
        ):

            for nombre_nodo, datos in update.items():

                mensajes = datos.get(
                    "messages",
                    []
                )

                for mensaje in mensajes:

                    # El agente solicita una herramienta
                    if (
                        nombre_nodo == "agent"
                        and getattr(
                            mensaje,
                            "tool_calls",
                            None
                        )
                    ):

                        for tool_call in mensaje.tool_calls:

                            trace.append(
                                {
                                    "tipo": "tool_call",
                                    "herramienta": tool_call["name"],
                                    "parametros": tool_call["args"]
                                }
                            )

                    # Resultado de una herramienta
                    elif nombre_nodo == "tools":

                        trace.append(
                            {
                                "tipo": "tool_result",
                                "contenido": mensaje.content
                            }
                        )

                    # Respuesta final
                    elif (
                        nombre_nodo == "agent"
                        and mensaje.content
                    ):

                        trace.append(
                            {
                                "tipo": "respuesta",
                                "contenido": mensaje.content
                            }
                        )

    with open(
        TRACE_PATH,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            trace,
            archivo,
            ensure_ascii=False,
            indent=4
        )

    print(
        f"Traza guardada en: {TRACE_PATH}"
    )


if __name__ == "__main__":
    asyncio.run(main())
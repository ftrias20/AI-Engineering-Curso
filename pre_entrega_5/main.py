import asyncio

from langchain_core.messages import HumanMessage

from agent import crear_app


async def main():

    config = {
        "configurable": {
            "thread_id": "soporte_memoria_01"
        },
        "recursion_limit": 10
    }

    async with crear_app() as app:

        print("\n--- Paso 1 ---")

        pregunta_1 = (
            "Que significa el error POS-999?"
        )

        print(
            f"Usuario: {pregunta_1}"
        )

        resultado_1 = await app.ainvoke(
            {
                "messages": [
                    HumanMessage(
                        content=pregunta_1
                    )
                ]
            },
            config=config
        )

        print(
            f"Agente: "
            f"{resultado_1['messages'][-1].content}"
        )


        print("\n--- Paso 2 ---")

        pregunta_2 = (
            "Y como lo resuelvo?"
        )

        print(
            f"Usuario: {pregunta_2}"
        )

        resultado_2 = await app.ainvoke(
            {
                "messages": [
                    HumanMessage(
                        content=pregunta_2
                    )
                ]
            },
            config=config
        )

        print(
            f"Agente: "
            f"{resultado_2['messages'][-1].content}"
        )


if __name__ == "__main__":
    asyncio.run(main())
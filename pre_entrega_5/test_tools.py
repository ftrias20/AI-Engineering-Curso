import asyncio

from tools import (
    buscar_incidente,
    obtener_procedimiento
)


async def main():

    print("--- Prueba 1: buscar incidente ---")

    incidente = await buscar_incidente.ainvoke(
        {
            "codigo_error": "POS-204"
        }
    )

    print(incidente)

    print("\n--- Prueba 2: obtener procedimiento ---")

    procedimiento = await obtener_procedimiento.ainvoke(
        {
            "procedimiento_id": "PROC-07"
        }
    )

    print(procedimiento)


if __name__ == "__main__":
    asyncio.run(main())
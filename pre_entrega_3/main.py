import asyncio

from rag import get_rag_response


async def main():

    # Pregunta cuya respuesta deberia estar en los documentos
    pregunta_valida = "Que es un patron de diseño?"

    print("=== PRUEBA 1: PREGUNTA VALIDA ===")
    print(f"Pregunta: {pregunta_valida}")

    respuesta_valida = await get_rag_response(
        pregunta_valida
    )

    print(f"Respuesta: {respuesta_valida.respuesta}")
    print(f"Referencias: {respuesta_valida.referencias}")


    # Pregunta que no tiene relacion con nuestros documentos
    pregunta_trampa = "Quien gano el mundial de futbol de 2022?"

    print("\n=== PRUEBA 2: PREGUNTA TRAMPA ===")
    print(f"Pregunta: {pregunta_trampa}")

    respuesta_trampa = await get_rag_response(
        pregunta_trampa
    )

    print(f"Respuesta: {respuesta_trampa.respuesta}")
    print(f"Referencias: {respuesta_trampa.referencias}")


if __name__ == "__main__":
    # Ejecuta el flujo asincrono
    asyncio.run(main())
import asyncio

from chain import process_text


async def main():
    # Texto tecnico que sera analizado por el pipeline
    texto = (
        "La API desarrollada con FastAPI utiliza Redis como cache "
        "y PostgreSQL para almacenar los datos. "
        "Actualmente el servicio esta caido porque se agotaron "
        "las conexiones disponibles a la base de datos."
    )

    print("Texto a procesar:")
    print(texto)

    try:
        # Ejecuta el pipeline de forma asincrona
        resultado = await process_text(texto)

        print("\nResultado validado:")

        # Convierte el objeto Pydantic a JSON para mostrarlo
        print(
            resultado.model_dump_json(indent=2)
        )

    except Exception as error:
        # Evita que el programa termine mostrando un error sin controlar
        print("\nNo se pudo procesar el texto.")
        print(f"Detalle: {error}")


if __name__ == "__main__":
    # Inicia el event loop y ejecuta la funcion asincrona main
    asyncio.run(main())
import asyncio


async def gpt_4_call() -> str:
    print("GPT-4: iniciando llamada")

    # Simulo una espera de red de 1 segundo
    await asyncio.sleep(1)

    print("GPT-4: respuesta recibida")
    return "Respuesta simulada de GPT-4"


async def claude_3_call() -> str:
    print("Claude 3: iniciando llamada")

    # Simulo una espera de red de 1.5 segundos
    await asyncio.sleep(1.5)

    print("Claude 3: respuesta recibida")
    return "Respuesta simulada de Claude 3"


async def local_llama_call() -> str:
    print("Llama local: iniciando llamada")

    # Simulo una espera de red de 3 segundos
    await asyncio.sleep(3)

    print("Llama local: respuesta recibida")
    return "Respuesta simulada de Llama local"


async def ejecutar_con_limite(
    numero: int,
    semaforo: asyncio.Semaphore,
    llamada_modelo
) -> str:
    # La tarea fue creada, pero todavia no tiene permiso
    print(f"Llamada {numero}: esperando turno")

    # Solo 2 llamadas pueden estar dentro de este bloque
    async with semaforo:
        print(f"Llamada {numero}: inicio")

        # Ejecuto la funcion del modelo recibida por parametro
        resultado = await llamada_modelo()

        print(f"Llamada {numero}: fin")
        return resultado


async def main():
    # Permito como maximo 2 llamadas al mismo tiempo
    semaforo = asyncio.Semaphore(2)

    # Guardo las funciones de los modelos
    modelos = [
        gpt_4_call,
        claude_3_call,
        local_llama_call
    ]

    # Aca voy a guardar las 10 corrutinas
    tareas = []

    # Genero numeros desde 1 hasta 10
    for numero in range(1, 11):
        # Alterno entre GPT, Claude y Llama
        posicion_modelo = (numero - 1) % len(modelos)
        modelo = modelos[posicion_modelo]

        # Creo la llamada usando el modelo seleccionado
        tarea = ejecutar_con_limite(
            numero,
            semaforo,
            modelo
        )

        # Guardo la llamada para ejecutarla despues
        tareas.append(tarea)

    try:
        # Toda la ejecucion tiene un limite maximo de 2 segundos
  
        async with asyncio.timeout(2):
            # Inicio las 10 llamadas respetando el limite del semaforo
            respuestas = await asyncio.gather(*tareas)

            print(f"Total de respuestas: {len(respuestas)}")

    except TimeoutError:
        # Controlo el error para que el programa no termine de forma inesperada
        print("Error: las llamadas superaron el tiempo maximo de 2 segundos")


if __name__ == "__main__":
   
    asyncio.run(main())
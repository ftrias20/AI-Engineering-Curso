import json
from pathlib import Path

from rag_system import RAGSystem


# Ruta del archivo con las preguntas de prueba
GOLDEN_SET_PATH = Path(__file__).parent / "golden_set.json"


def cargar_golden_set():

    # Lee las preguntas y documentos esperados
    with open(
        GOLDEN_SET_PATH,
        "r",
        encoding="utf-8"
    ) as archivo:

        return json.load(archivo)


def evaluar():

    # Crea el sistema de busqueda hibrida
    rag = RAGSystem()

    # Carga los casos de prueba
    golden_set = cargar_golden_set()

    precisiones = []
    recalls = []

    for caso in golden_set:

        pregunta = caso["pregunta"]
        documento_esperado = caso["documento_id_esperado"]

        # Recupera los 5 resultados
        resultados = rag.buscar(
            pregunta
        )

        # Obtiene los nombres de los archivos recuperados
        fuentes = [
            documento.metadata["source"]
            for documento in resultados
        ]

        # Cuenta cuantos resultados pertenecen
        # al documento esperado
        relevantes = fuentes.count(
            documento_esperado
        )

        # Precision@5
        precision = relevantes / 5

        # Recall@5
        recall = (
            1
            if documento_esperado in fuentes
            else 0
        )

        precisiones.append(
            precision
        )

        recalls.append(
            recall
        )

        print("\n----------------------------------")
        print(f"Pregunta: {pregunta}")
        print(
            f"Documento esperado: "
            f"{documento_esperado}"
        )

        print("Top 5:")

        for indice, fuente in enumerate(
            fuentes,
            start=1
        ):
            print(
                f"{indice}. {fuente}"
            )

        print(
            f"Precision@5: {precision:.2f}"
        )

        print(
            f"Recall@5: {recall:.2f}"
        )

    # Calcula el promedio de todas las preguntas
    precision_promedio = (
        sum(precisiones) / len(precisiones)
    )

    recall_promedio = (
        sum(recalls) / len(recalls)
    )

    print("\n==================================")
    print("RESUMEN DE EVALUACION")
    print("==================================")

    print(
        f"Precision@5 promedio: "
        f"{precision_promedio:.2f}"
    )

    print(
        f"Recall@5 promedio: "
        f"{recall_promedio:.2f}"
    )


if __name__ == "__main__":
    evaluar()
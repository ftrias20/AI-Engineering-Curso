from pydantic import BaseModel, Field
from langchain_core.tools import tool


# Simulacion de una base de incidentes tecnicos
INCIDENTES_DB = {
    "POS-204": {
        "codigo": "POS-204",
        "descripcion": "Perdida de comunicacion con la terminal de pago",
        "categoria": "comunicaciones",
        "procedimiento_id": "PROC-07"
    },
    "DB-500": {
        "codigo": "DB-500",
        "descripcion": "Error de conexion con la base de datos",
        "categoria": "base_de_datos",
        "procedimiento_id": "PROC-12"
    }
}


# Simulacion de procedimientos tecnicos
PROCEDIMIENTOS_DB = {
    "PROC-07": {
        "procedimiento_id": "PROC-07",
        "titulo": "Restablecer comunicacion con terminal",
        "pasos": [
            "Verificar conectividad de red",
            "Validar que la terminal este disponible",
            "Reiniciar la conexion con el dispositivo"
        ]
    },
    "PROC-12": {
        "procedimiento_id": "PROC-12",
        "titulo": "Restablecer conexion con base de datos",
        "pasos": [
            "Verificar disponibilidad del servidor",
            "Validar cadena de conexion",
            "Reintentar la conexion"
        ]
    }
}


class BuscarIncidenteInput(BaseModel):
    codigo_error: str = Field(
        description="Codigo tecnico del error a consultar"
    )


class ObtenerProcedimientoInput(BaseModel):
    procedimiento_id: str = Field(
        description="Identificador del procedimiento tecnico"
    )


@tool(args_schema=BuscarIncidenteInput)
async def buscar_incidente(
    codigo_error: str
) -> dict[str, object]:
    """
    Busca informacion tecnica sobre un codigo de error.

    Usa esta herramienta cuando el usuario informa un codigo
    de error y necesitas conocer su descripcion, categoria
    o el procedimiento asociado para resolverlo.
    """

    incidente = INCIDENTES_DB.get(
        codigo_error.upper()
    )

    if incidente is None:
        return {
            "error": f"No se encontro el codigo {codigo_error}"
        }

    return incidente


@tool(args_schema=ObtenerProcedimientoInput)
async def obtener_procedimiento(
    procedimiento_id: str
) -> dict[str, object]:
    """
    Obtiene los pasos de resolucion de un procedimiento tecnico.

    Usa esta herramienta cuando ya conoces el identificador
    de un procedimiento y necesitas saber los pasos necesarios
    para resolver el incidente.
    """

    procedimiento = PROCEDIMIENTOS_DB.get(
        procedimiento_id.upper()
    )

    if procedimiento is None:
        return {
            "error": (
                f"No se encontro el procedimiento "
                f"{procedimiento_id}"
            )
        }

    return procedimiento


tools = [
    buscar_incidente,
    obtener_procedimiento
]
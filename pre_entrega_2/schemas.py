from enum import Enum

from pydantic import BaseModel, Field


class NivelCriticidad(str, Enum):
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"


class TechnicalExtraction(BaseModel):
    # Debe detectar al menos una tecnologia
    tecnologias: list[str] = Field(min_length=1)

    # Solo acepta baja, media o alta
    nivel_de_criticidad: NivelCriticidad

    # El resumen no puede estar vacio
    resumen_tecnico: str = Field(min_length=1)


if __name__ == "__main__":
    resultado = TechnicalExtraction(
        tecnologias=["FastAPI", "Redis", "PostgreSQL"],
        nivel_de_criticidad="alta",
        resumen_tecnico="API con cache y persistencia en base de datos."
    )

    print(resultado)
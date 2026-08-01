# Pre-entrega 2 - Pipeline de procesamiento validado

Pipeline asíncrono desarrollado con LangChain para analizar textos técnicos y devolver un objeto validado con Pydantic.

El sistema extrae:

- Tecnologías mencionadas.
- Nivel de criticidad: baja, media o alta.
- Resumen técnico.

## Estructura

```text
pre_entrega_2/
├── schemas.py
├── chain.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Requisitos

- Python 3.12.
- Una API key válida de OpenAI.

## Crear y activar el entorno virtual

Desde la raíz del repositorio:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

## Instalar dependencias

```powershell
python -m pip install -r .\pre_entrega_2\requirements.txt
```

## Configurar variables de entorno

Crear un archivo `.env` en la raíz del repositorio con:

```env
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini
LLM_TEMPERATURE=0
```

El archivo `.env` contiene la clave real y no debe subirse al repositorio.

## Ejecutar el proyecto

Desde la raíz del repositorio:

```powershell
python .\pre_entrega_2\main.py
```

## Funcionamiento

El pipeline utiliza:

- `ChatPromptTemplate` para construir el prompt.
- `ChatOpenAI` para consultar el modelo.
- `with_structured_output()` para obtener una salida compatible con el esquema Pydantic.
- LCEL para conectar el prompt y el modelo.
- `with_retry()` para realizar hasta tres intentos ante errores.
- `.ainvoke()` para ejecutar la cadena de forma asíncrona.

## Ejemplo de salida

```json
{
  "tecnologias": [
    "FastAPI",
    "Redis",
    "PostgreSQL"
  ],
  "nivel_de_criticidad": "alta",
  "resumen_tecnico": "El servicio se encuentra caído debido al agotamiento de conexiones disponibles a PostgreSQL."
}
```

## Manejo de errores

La función `process_text()` registra el inicio y el resultado del procesamiento.

Si la ejecución falla después de los reintentos, el error se registra y es manejado por el script de prueba para evitar una finalización inesperada.
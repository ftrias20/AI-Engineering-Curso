# Pre-entrega 1 - Unified Async LLM Client

Cliente asíncrono unificado desarrollado en Python 3.12 para trabajar con los proveedores OpenAI y Anthropic mediante una interfaz común.

El proveedor se selecciona mediante una variable de configuración, sin modificar el código principal.

## Funcionalidades

- Cliente asíncrono para OpenAI mediante `AsyncOpenAI`.
- Cliente asíncrono para Anthropic mediante `AsyncAnthropic`.
- Generación de respuestas completas.
- Generación mediante streaming.
- Validación de mensajes y configuración con Pydantic.
- Selección del proveedor mediante `AsyncLLMManager`.
- Manejo controlado de errores.
- Configuración mediante variables de entorno.

## Estructura

```text
pre_entrega_1/
├── schemas.py
├── base_client.py
├── openai_client.py
├── anthropic_client.py
├── llm_manager.py
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

## Requisitos

- Python 3.12.
- Una API key válida de OpenAI o Anthropic.

## Crear el entorno virtual

Desde la raíz del repositorio:

```powershell
python -m venv .venv
```

Activar el entorno virtual en Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Instalar dependencias

Desde la raíz del repositorio:

```powershell
python -m pip install -r .\pre_entrega_1\requirements.txt
```

Las dependencias utilizadas son:

```text
openai
anthropic
pydantic
python-dotenv
```

## Configurar variables de entorno

Copiar el archivo de ejemplo:

```powershell
Copy-Item .\pre_entrega_1\.env.example .\.env
```

Completar el archivo `.env` ubicado en la raíz del repositorio:

```env
LLM_PROVIDER=openai
LLM_TEMPERATURE=0
LLM_MAX_TOKENS=300

OPENAI_API_KEY=
OPENAI_MODEL=gpt-4o-mini

ANTHROPIC_API_KEY=
ANTHROPIC_MODEL=
```

Para utilizar OpenAI:

```env
LLM_PROVIDER=openai
```

Para utilizar Anthropic:

```env
LLM_PROVIDER=anthropic
```

También debe configurarse la API key y el modelo correspondientes al proveedor seleccionado.

## Ejecutar el script de prueba

Desde la raíz del repositorio:

```powershell
python .\pre_entrega_1\main.py
```

El script realiza la siguiente pregunta:

```text
¿Que es la inteligencia artificial? Explicalo de forma breve y sencilla.
```

La consulta se ejecuta en dos modalidades:

1. Respuesta completa mediante `generate()`.
2. Respuesta progresiva mediante `stream()`.

## Manejo de errores

Los clientes capturan las excepciones producidas durante las llamadas a las APIs y devuelven un error controlado para evitar que el programa finalice inesperadamente.

Esto contempla errores como:

- Problemas de conexión.
- API key inválida.
- Falta de cuota.
- Límite de solicitudes.
- Modelo no disponible.
- Configuración inválida.

## Seguridad

El archivo `.env` contiene las claves reales por eso no se sube al repo

El archivo `.gitignore` debe incluir:

```gitignore
.env
.venv/
__pycache__/
```

El archivo `.env.example` sí debe incluirse en el repo porque no contiene claves privadas.

## Estado de las pruebas

La implementación fue probada con OpenAI en:

- Modo de respuesta completa.
- Modo streaming.
- Lectura de configuración desde `.env`.
- Validación de temperatura y cantidad máxima de tokens.
- Creación del cliente mediante `AsyncLLMManager`.

La integración con Anthropic se encuentra implementada utilizando el SDK oficial asíncrono. Para realizar una prueba real es necesario configurar una API key válida y el modelo correspondiente.
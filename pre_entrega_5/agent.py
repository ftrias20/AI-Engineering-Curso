import os
from contextlib import asynccontextmanager
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState, START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

from tools import tools


# Carga el .env ubicado en la raiz del proyecto
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)

# Archivo donde se guarda la memoria del agente
DB_PATH = Path(__file__).parent / "agent_memory.db"

# Modelo configurado para el agente
MODEL_NAME = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o-mini"
)


# Crea el modelo
llm = ChatOpenAI(
    model=MODEL_NAME,
    temperature=0
)

# Vincula las herramientas al modelo
llm_with_tools = llm.bind_tools(
    tools,
    parallel_tool_calls=False
)



# Mensaje con las reglas generales del agente
SYSTEM_MESSAGE = SystemMessage(
    content=(
        "Sos un asistente de soporte tecnico. "
        "Usa las herramientas disponibles cuando necesites "
        "consultar informacion sobre incidentes o procedimientos. "
        "No inventes informacion tecnica. "
        "No llames dos veces a la misma herramienta con los mismos "
        "parametros si ya obtuviste una respuesta valida. "
        "Si el resultado de una herramienta indica que existe "
        "un procedimiento relacionado y necesitas sus pasos, "
        "consulta la herramienta correspondiente antes de responder."
    )
)

async def call_model(
    state: MessagesState
) -> dict:

    # Agrega las instrucciones del sistema al historial
    messages = [
        SYSTEM_MESSAGE,
        *state["messages"]
    ]

    # El modelo analiza los mensajes y decide que hacer
    response = await llm_with_tools.ainvoke(
        messages
    )

    # Agrega la respuesta del modelo al estado
    return {
        "messages": [response]
    }


# Crea el grafo
workflow = StateGraph(
    MessagesState
)

# Nodo donde razona el modelo
workflow.add_node(
    "agent",
    call_model
)

# Nodo encargado de ejecutar herramientas
workflow.add_node(
    "tools",
    ToolNode(tools)
)

# El flujo comienza en el agente
workflow.add_edge(
    START,
    "agent"
)

# Decide si el agente quiere ejecutar una tool o terminar
workflow.add_conditional_edges(
    "agent",
    tools_condition
)

# Luego de ejecutar una tool vuelve al agente
workflow.add_edge(
    "tools",
    "agent"
)


@asynccontextmanager
async def crear_app():

    # Abre la conexion SQLite para guardar la memoria
    async with AsyncSqliteSaver.from_conn_string(
        str(DB_PATH)
    ) as memory:

        # Compila el grafo usando persistencia
        app = workflow.compile(
            checkpointer=memory
        )

        yield app
# Pre-entrega 5 - Agente de razonamiento ciclico con LangGraph

## Descripcion

Este proyecto implementa un agente de soporte tecnico utilizando LangGraph.

El agente puede:

- Analizar una consulta del usuario.
- Decidir de forma autonoma cuando utilizar una herramienta.
- Ejecutar herramientas tecnicas.
- Utilizar el resultado de una herramienta para decidir si necesita otra.
- Mantener el historial de una conversacion mediante SQLite y thread_id.
- Manejar errores o informacion no encontrada sin inventar una solucion.
- Generar una traza JSON con las herramientas utilizadas durante la ejecucion.

## Escenario

El agente trabaja sobre una base simulada de incidentes tecnicos.

Por ejemplo, ante la consulta:

```text
El sistema muestra el error POS-204.
Decime que significa y como tengo que resolverlo.
import json
import datetime
from .ollama_client import generar_respuesta

def desglosar_objetivo(objetivo, contexto=""):
    """
    Envía un objetivo a un LLM (DeepSeek, Claude, etc.) y obtiene una lista de subtareas.
    """
    prompt = f"""
Eres un asistente especializado en descomponer objetivos complejos en tareas claras y accionables.

Objetivo: {objetivo}

Contexto adicional:
{contexto}

Devuelve la lista en formato JSON con los siguientes campos:
- tarea: descripción corta de la acción
- tipo: ['investigación', 'programación', 'redacción', etc.]
- prioridad: número (1 alta, 5 baja)
- depende_de: lista de otras tareas si aplica

Ejemplo de salida:
[
  {{
    "tarea": "Investigar artículos recientes sobre IA en educación",
    "tipo": "investigación",
    "prioridad": 1,
    "depende_de": []
  }},
  ...
]
"""
    respuesta = generar_respuesta(prompt)
    try:
        tareas = json.loads(respuesta)
    except json.JSONDecodeError:
        tareas = [{"error": "No se pudo interpretar la respuesta del modelo", "crudo": respuesta}]
    
    return {
        "objetivo": objetivo,
        "contexto": contexto,
        "tareas": tareas,
        "fecha": str(datetime.datetime.now())
    }

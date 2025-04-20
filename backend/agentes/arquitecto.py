import json
import datetime
from .ollama_client import generar_respuesta

def generar_plan_estructurado(objetivo: str, contexto: str = "") -> dict:
    """
    El arquitecto descompone un objetivo complejo en un conjunto de tareas estructuradas,
    devolviendo un plan claro y ejecutable en formato JSON.
    """

    prompt = f"""
Eres un arquitecto de soluciones. Tu tarea es descomponer objetivos complejos en un plan de trabajo
detallado, con tareas bien definidas, prioridades, tipos y dependencias.

Objetivo: {objetivo}

Contexto adicional:
{contexto}

Devuelve la lista de tareas en formato JSON con los siguientes campos:
- tarea: descripción corta de la acción
- tipo: ['investigación', 'programación', 'redacción', etc.]
- prioridad: número del 1 (alta) al 5 (baja)
- depende_de: lista de otras tareas si aplica

Ejemplo de salida:
[
  {{
    "tarea": "Investigar artículos recientes sobre IA en educación",
    "tipo": "investigación",
    "prioridad": 1,
    "depende_de": []
  }},
  {{
    "tarea": "Escribir una introducción general sobre IA en educación",
    "tipo": "redacción",
    "prioridad": 2,
    "depende_de": ["Investigar artículos recientes sobre IA en educación"]
  }}
]
"""

    respuesta = generar_respuesta(prompt)

    try:
        tareas = json.loads(respuesta)
    except json.JSONDecodeError:
        tareas = [{
            "tarea": "Error de interpretación",
            "tipo": "error",
            "prioridad": 1,
            "depende_de": [],
            "error": "No se pudo interpretar la respuesta del modelo",
            "respuesta_cruda": respuesta
        }]

    return {
        "objetivo": objetivo,
        "contexto": contexto,
        "tareas": tareas,
        "agente": "arquitecto",
        "fase": "planificacion",
        "timestamp": datetime.datetime.utcnow().isoformat()
    }

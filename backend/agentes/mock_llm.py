# agentes/mock_llm.py

import json
from datetime import datetime

contador = {"valor": 0}

def respuesta_simulada(tipo="codigo", prompt="...", agente="arquitecto"):
    contador["valor"] += 1

    if tipo == "codigo":
        return f"# Simulación de código Python\n\ndef ejemplo():\n    return 'Hola mundo {contador['valor']}'"

    if tipo == "evaluacion":
        return f"La respuesta fue evaluada correctamente en base al criterio solicitado. Simulación {contador['valor']}."

    if tipo == "arquitecto":
        return json.dumps([
            {
                "tarea": "Analizar requerimientos del sistema",
                "tipo": "investigación",
                "prioridad": 1,
                "depende_de": []
            },
            {
                "tarea": "Diseñar arquitectura básica",
                "tipo": "programación",
                "prioridad": 2,
                "depende_de": ["Analizar requerimientos del sistema"]
            },
            {
                "tarea": "Configurar entorno de desarrollo",
                "tipo": "infraestructura",
                "prioridad": 3,
                "depende_de": []
            }
        ], indent=2)

    if tipo == "asistente":
        return f"Asistente generando contenido simulado según el plan entregado. Iteración: {contador['valor']}"

    # fallback genérico
    return f"[{agente.upper()}] Respuesta simulada #{contador['valor']} - Tipo: {tipo} - Prompt: {prompt[:50]}..."

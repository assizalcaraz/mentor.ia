import os
import requests
from . import prompts

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://ollama:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "codellama:7b-instruct")


def generar_respuesta(prompt, temperatura=0.2, modelo="codellama:7b-instruct"):
    url = f"{OLLAMA_API_URL}/api/generate"

    # Si prompt ya es un dict con todas las claves, no lo empaquetes de nuevo
    payload = prompt if isinstance(prompt, dict) else {
        "model": modelo,
        "prompt": prompt,
        "temperature": temperatura,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "Error: no se recibió respuesta del modelo.")
    except requests.exceptions.HTTPError as http_err:
        return f"Error HTTP: {http_err} - Payload enviado: {payload}"
    except Exception as e:
        return f"Error inesperado: {e} - Payload enviado: {payload}"


def generar_respuesta_desde_template(tipo, **kwargs):
    if tipo == "codigo":
        payload = prompts.prompt_codigo(**kwargs)
    elif tipo == "constructor":
        payload = prompts.prompt_constructor(**kwargs)
    elif tipo == "evaluacion":
        payload = prompts.prompt_evaluacion(**kwargs)
    else:
        raise ValueError("Tipo de prompt no reconocido")

    return enviar_a_ollama(payload)


def enviar_a_ollama(payload):
    url = f"{OLLAMA_API_URL}/api/generate"
    try:
        response = requests.post(url, json=payload, timeout=90)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "Error: no se recibió respuesta del modelo.")
    except requests.exceptions.HTTPError as http_err:
        return f"Error HTTP: {http_err} - Payload: {payload}"
    except Exception as e:
        return f"Error inesperado: {e} - Payload: {payload}"

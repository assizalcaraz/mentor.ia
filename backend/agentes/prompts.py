# agentes/prompts.py

BASE_PROMPT = """\
Tu tarea es responder exclusivamente en formato JSON válido y sin explicaciones adicionales. 
No incluyas texto antes ni después del bloque JSON. 
Asegurate de que sea un JSON parseable por una máquina. 
"""

def prompt_codigo(prompt_usuario, temperatura=0.2, modelo="codellama:7b-instruct"):
    prompt = (
        "Respondé solo con el código, en formato JSON si es posible. "
        "No expliques nada. No incluyas encabezados ni texto fuera del bloque de código.\n"
        f"INSTRUCCIÓN: {prompt_usuario}"
    )
    return {
        "model": modelo,
        "prompt": prompt,
        "temperature": temperatura,
        "stream": False
    }


def prompt_constructor(objetivo, contexto="", temperatura=0.2, modelo="phind-codellama"):
    full_prompt = f"""{BASE_PROMPT}
Analizá el siguiente objetivo: "{objetivo}"
{f'Contexto: {contexto}' if contexto else ''}

Devuelve una lista JSON de tareas necesarias para cumplirlo. 
Cada tarea debe tener: id, descripcion, prioridad (alta/media/baja).

Formato esperado:
[
  {{
    "id": 1,
    "descripcion": "Inicializar repositorio git",
    "prioridad": "alta"
  }},
  ...
]"""
    return {
        "model": modelo,
        "prompt": full_prompt,
        "temperature": temperatura,
        "stream": False
    }

def prompt_evaluacion(texto, criterio="calidad técnica", temperatura=0.2, modelo="phind-codellama"):
    full_prompt = f"""{BASE_PROMPT}
Evaluá el siguiente texto según el criterio '{criterio}'.

Texto:
{texto}

Formato esperado:
{{
  "criterio": "{criterio}",
  "calificacion": <número del 1 al 10>,
  "justificacion": "<breve justificación>"
}}"""
    return {
        "model": modelo,
        "prompt": full_prompt,
        "temperature": temperatura,
        "stream": False
    }

# 💡 Extra: para casos de metadata, info estructurada, etc.
def prompt_info(categoria, temperatura=0.2, modelo="phind-codellama"):
    full_prompt = f"""{BASE_PROMPT}
Devolveme información relevante sobre la categoría "{categoria}" en formato JSON.

Formato esperado:
{{
  "categoria": "{categoria}",
  "datos": [
    "...",
    "..."
  ]
}}"""
    return {
        "model": modelo,
        "prompt": full_prompt,
        "temperature": temperatura,
        "stream": False
    }

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time

from .ollama_client import generar_respuesta
from .constructor import desglosar_objetivo
from .prompts import prompt_codigo

@csrf_exempt
def medir_tiempo_llm(request):
    prompt_usuario = request.GET.get("prompt", "¿Cuál es la capital de Argentina?")
    temperatura = float(request.GET.get("temperatura", 0.2))
    modelo = request.GET.get("modelo", "codellama:7b-instruct")

    prompt_dict = prompt_codigo(prompt_usuario, temperatura, modelo)

    start = time.time()
    respuesta = generar_respuesta(prompt_dict)
    end = time.time()

    return JsonResponse({
        "respuesta": respuesta,
        "duracion_segundos": round(end - start, 2)
    })

def generar_respuesta_llm(request):
    prompt_usuario = request.GET.get("prompt", "Escribí una función en Python que devuelva Fibonacci")
    temperatura = float(request.GET.get("temperatura", 0.2))
    modelo = request.GET.get("modelo", "codellama:7b-instruct")

    prompt_dict = prompt_codigo(prompt_usuario, temperatura, modelo)
    respuesta = generar_respuesta(prompt_dict)

    return JsonResponse({"respuesta": respuesta})

def constructor_view(request):
    objetivo = request.GET.get("objetivo", "Crear una app de asistencia con reconocimiento facial")
    contexto = request.GET.get("contexto", "")
    resultado = desglosar_objetivo(objetivo, contexto)
    return JsonResponse(resultado, safe=False)

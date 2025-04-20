from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time

from .arquitecto import generar_plan_estructurado
from .context_manager import guardar_interaccion


@csrf_exempt
def planificar_objetivo(request):
    if request.method != "POST":
        return JsonResponse({"error": "Sólo se permiten solicitudes POST."}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
        objetivo = data.get("objetivo", "Construir un asistente personal para gestionar mi agenda semanal")
        contexto = data.get("contexto", "")
        objetivo_id = data.get("objetivo_id", f"objetivo_{int(time.time())}")

        plan = generar_plan_estructurado(objetivo, contexto)
        tareas = plan.get("tareas", [])

        # Guardar cada tarea en Chroma con metadatos
        for tarea in tareas:
            guardar_interaccion(
                contenido=tarea,
                agente="arquitecto",
                objetivo_id=objetivo_id,
                fase="planificacion"
            )

        return JsonResponse({
            "mensaje": "Planificación realizada correctamente",
            "objetivo_id": objetivo_id,
            "plan": plan
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({"error": str(e)}, status=500)

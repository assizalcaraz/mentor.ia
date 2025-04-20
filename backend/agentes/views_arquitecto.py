from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time
import traceback

from .arquitecto import generar_plan_estructurado
from .context_manager import guardar_interaccion


@csrf_exempt
def planificar_objetivo(request):
    if request.method != "POST":
        return JsonResponse({"error": "Sólo se permiten solicitudes POST."}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
        objetivo = data.get("objetivo")
        contexto = data.get("contexto", "")
        objetivo_id = data.get("objetivo_id", f"objetivo_{int(time.time())}")

        if not objetivo:
            return JsonResponse({"error": "Se requiere un 'objetivo'"}, status=400)

        plan = generar_plan_estructurado(objetivo, contexto)
        tareas = plan.get("tareas", [])

        for tarea in tareas:
            guardar_interaccion(
                texto=json.dumps(tarea, ensure_ascii=False),
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
        traceback.print_exc()
        return JsonResponse({"error": str(e)}, status=500)

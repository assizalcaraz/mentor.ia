from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time
import traceback

from .arquitecto import generar_plan_estructurado
from .context_manager import guardar_interaccion
from .ollama_client import verificar_config
from .models import Objetivo, Roadmap, Tarea

from django.utils import timezone

@csrf_exempt
def planificar_objetivo(request):
    verificar_config()
    if request.method != "POST":
        return JsonResponse({"error": "Sólo se permiten solicitudes POST."}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
        titulo = data.get("objetivo")
        descripcion = data.get("contexto", "")
        prioridad = data.get("prioridad", 3)  # opcional, por defecto 3

        if not titulo:
            return JsonResponse({"error": "Se requiere un 'objetivo'"}, status=400)

        # Paso 1: buscar o crear Objetivo
        objetivo, creado = Objetivo.objects.get_or_create(
            titulo=titulo,
            defaults={
                "descripcion": descripcion,
                "prioridad": prioridad,
                "fecha_creacion": timezone.now()
            }
        )

        # Paso 2: generar plan desde LLM
        plan = generar_plan_estructurado(titulo, descripcion)
        tareas_llm = plan.get("tareas", [])

        # Paso 3: crear Roadmap asociado
        roadmap = Roadmap.objects.create(
            objetivo=objetivo,
            generado_por="arquitecto"
        )

        tareas_guardadas = []

        # Paso 4: registrar tareas
        for tarea_data in tareas_llm:
            if not isinstance(tarea_data, dict):
                continue  # saltar si alguna viene corrupta

            tarea_obj = Tarea.objects.create(
                roadmap=roadmap,
                tarea=tarea_data.get("tarea", ""),
                tipo=tarea_data.get("tipo", "sin_tipo"),
                prioridad=tarea_data.get("prioridad", 3),
                depende_de=tarea_data.get("depende_de", []),
                actor=tarea_data.get("actor", "asistente")
            )

            # Registrar en base vectorial (ChromaDB)
            guardar_interaccion(
                texto=json.dumps(tarea_data, ensure_ascii=False),
                agente="arquitecto",
                objetivo_id=str(objetivo.id),
                fase="planificacion"
            )

            tareas_guardadas.append(tarea_obj.id)

        return JsonResponse({
            "mensaje": "Planificación realizada correctamente",
            "objetivo_id": objetivo.id,
            "roadmap_id": roadmap.id,
            "tareas_guardadas": tareas_guardadas,
            "plan": plan
        })

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({"error": str(e)}, status=500)
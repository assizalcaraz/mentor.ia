from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from agentes.models import Objetivo, Roadmap, Tarea

@csrf_exempt
def limpiar_base(request):
    if request.method != "POST":
        return JsonResponse({"error": "Sólo permitido método POST"}, status=405)

    try:
        Tarea.objects.all().delete()
        Roadmap.objects.all().delete()
        Objetivo.objects.all().delete()

        return JsonResponse({"mensaje": "Base de datos limpiada exitosamente."})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

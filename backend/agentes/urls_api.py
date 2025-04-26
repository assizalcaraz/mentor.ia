# backend/agentes/urls_api.py
from django.urls import path
from .views import (
    simular_interaccion,
    consultar_memoria,
    historial_compilado,
    interactuar,
    medir_tiempo_llm,
    generar_respuesta_llm,
    arquitecto_view,
)
from .views_arquitecto import (
    planificar_objetivo,
)
from .views_asistente import (
    ejecutar_tareas,

)

from tools.views_tools import (
    limpiar_base,
    
)

urlpatterns = [
    path("simular/", simular_interaccion, name="simular_interaccion"),
    path("memoria/", consultar_memoria, name="consultar_memoria"),
    path("historial/", historial_compilado, name="historial_compilado"),
    path("interactuar/", interactuar, name="interactuar_llm"),
    path("tiempo/", medir_tiempo_llm, name="medir_tiempo_llm"),
    path("generar/", generar_respuesta_llm, name="generar_respuesta"),
    path("arquitecto/", arquitecto_view, name="arquitecto_view"),
    path("arquitecto/planificar/", planificar_objetivo, name="planificar_objetivo"),
    path("asistente/ejecutar/", ejecutar_tareas, name="ejecutar_tareas_asistente"),
    path("tools/limpiar_base/", limpiar_base, name="limpiar_base"),




]

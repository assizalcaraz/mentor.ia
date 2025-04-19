from django.urls import path
from .views import (
    generar_respuesta_llm,
    constructor_view,
    medir_tiempo_llm,
    interactuar,
    procesar_consulta_llm,
)

urlpatterns = [
    path("generar/", generar_respuesta_llm, name="generar_respuesta"),
    path("constructor/", constructor_view, name="constructor_view"),
    path("tiempo/", medir_tiempo_llm, name="medir_tiempo_llm"),
    path("interactuar/", interactuar, name="interactuar_llm"),
    path("procesar/", procesar_consulta_llm, name="procesar_consulta"),
]

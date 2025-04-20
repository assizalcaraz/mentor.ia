from django.urls import path
from .views import (
    generar_respuesta_llm,
    arquitecto_view,
    medir_tiempo_llm,
    interactuar,
    
)
from .views_arquitecto import (
    planificar_objetivo
)
#from .views_sandbox import procesar_consulta_llm


urlpatterns = [
    path("generar/", generar_respuesta_llm, name="generar_respuesta"),
    path("arquitecto/", arquitecto_view, name="arquitecto_view"),
    path("tiempo/", medir_tiempo_llm, name="medir_tiempo_llm"),
    path("interactuar/", interactuar, name="interactuar_llm"),
    #path("procesar/", procesar_consulta_llm)

    #Arquitecto
    path("arquitectar/", planificar_objetivo, name="planificar_objetivo"),

]

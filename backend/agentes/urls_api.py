# agentes/urls_api.py

from django.urls import path
from .views import (
    simular_interaccion,
    consultar_memoria,
    historial_compilado
)

urlpatterns = [
    path("simular/", simular_interaccion, name="simular_interaccion"),
    path("memoria/", consultar_memoria, name="consultar_memoria"),
    path("historial/", historial_compilado, name="historial_compilado"),

]

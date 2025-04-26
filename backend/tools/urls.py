# tools/urls.py

from django.urls import path
from tools.views_tools import limpiar_base

urlpatterns = [
    path('limpiar_base/', limpiar_base, name='limpiar_base'),
]

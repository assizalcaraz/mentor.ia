from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("agentes/", include("agentes.urls")),
    path("agentes/", include("agentes.urls_api")),


]

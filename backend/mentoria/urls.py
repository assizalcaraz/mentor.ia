from django.contrib import admin
from django.urls import path, include
from agentes import urls_api 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("agentes/", include("agentes.urls")),
    path('tools/', include('tools.urls')), 
    path("api/", include(urls_api)), 


]

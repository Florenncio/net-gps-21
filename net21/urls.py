import clientes
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from clientes import views
from rest_framework import routers, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('equipamentos/', include('equipamentos.urls')),
    path('localizacoes/', include('localizacoes.urls')),
]
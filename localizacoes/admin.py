from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Localizacao

admin.site.register(Localizacao)

class LocalizacaoAdmin(Localizacao):
    default_lon = -7.1283946703750765
    default_lat = -34.86398070745317
    default_zoom = 12


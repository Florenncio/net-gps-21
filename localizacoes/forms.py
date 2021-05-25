from django import forms
from django.forms import fields
from .models import Localizacao
from django.contrib.gis import forms

class LocalizacaoForm (forms.Form):
    point = forms.PointField(widget=
        forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
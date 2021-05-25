from django.shortcuts import render
from django.views.generic import ListView, CreateView, FormView
from .models import Localizacao
from .forms import LocalizacaoForm
from django.urls import reverse_lazy


class LocalizacaoList (ListView):
    queryset = Localizacao.objects.filter(ponto_loc__isnull=False)
    template_name = 'map.html'
    context_object_name = 'point_list'

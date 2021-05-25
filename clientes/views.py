from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Cliente
from .forms import ClienteForm

class ClienteListView (ListView):
    context_object_name = 'cliente_list'
    template_name = 'list-cliente.html'

    def get_queryset(self):
        return Cliente.objects.all()

class ClienteDetailView (DetailView):
    model = Cliente
    template_name = 'detail-cliente.html'
    success_url = reverse_lazy('list-cliente')

class ClienteCreateView(CreateView):
    form_class = ClienteForm
    template_name = "create-cliente.html"
    success_url = reverse_lazy('list-cliente')

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "confirm-delete.html"
    success_url = reverse_lazy('list-cliente')

class ClienteUpdateView(UpdateView):
    form_class = ClienteForm
    template_name = "update-cliente.html"
    success_url = reverse_lazy('list-cliente')

    def get_queryset(self):
        return Cliente.objects.all()

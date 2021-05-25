from django.urls import path, include
from .views import LocalizacaoList, LocalizacaoForm

urlpatterns = [
    path('', LocalizacaoList.as_view(), name='map'),
]
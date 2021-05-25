from django.urls import path, include
from clientes import views, api
from rest_framework import routers

api_router = routers.DefaultRouter()
api_router.register(r'rest', api.ClienteViewSet)

urlpatterns = [
    path('api/', include(api_router.urls)),
    path('', views.ClienteListView.as_view(), name='list-cliente'),
    path('<int:pk>', views.ClienteDetailView.as_view(), name = 'detail-cliente'),
    path('update/<int:pk>', views.ClienteUpdateView.as_view(), name='update-cliente'),
    path('create', views.ClienteCreateView.as_view(), name = 'create-cliente'),
    path('delete/<int:pk>', views.ClienteDeleteView.as_view(), name='delete-cliente'),
]

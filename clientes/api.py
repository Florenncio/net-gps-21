from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ClienteSerialize
from .models import Cliente


class ClienteViewSet (viewsets.ModelViewSet): 
    serializer_class = ClienteSerialize
    queryset =  Cliente.objects.all().order_by('nome_cli')
    '''permission_classes = [permissions.IsAuthenticated]'''
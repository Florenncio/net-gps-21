from django.db.models import fields
from rest_framework import serializers
from .models import Cliente

class ClienteSerialize (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Creación de la Priera Vista
class ApiEmployerView(viewsets.ModelViewSet):
	queryset = models.ApiEmployer.objects.all()
	serializer_class = serializers.ApiEmployerSerializer

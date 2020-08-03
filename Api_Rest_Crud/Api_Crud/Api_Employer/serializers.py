from rest_framework import serializers
from .models import ApiEmployer

# Creación del Primer Serializer
class ApiEmployerSerializer(serializers.ModelSerializer):
	class Meta:
		model = ApiEmployer
		fields = '__all__'
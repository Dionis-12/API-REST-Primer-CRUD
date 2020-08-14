from rest_framework import serializers
from .models import Employers

# Creación del Primer Serializer
class ApiEmployerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employers
		fields = '__all__'
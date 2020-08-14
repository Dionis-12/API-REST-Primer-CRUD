from django.db import models

# Creación del Primer Modelo
class Employers(models. Model):
	Name = models.CharField(verbose_name = 'Nombre Completo', max_length = 50)
	Last_Name = models.CharField(verbose_name = 'Apellido Completo', max_length = 100)
	Pais = models.CharField(verbose_name = 'Pais de Nacimiento', max_length = 50)
	Country = models.CharField(verbose_name = 'Ciudad de Nacimiento', max_length = 50)
	Phone = models.CharField(verbose_name = 'Número Telefónico', max_length = 15)
	Email = models.EmailField(verbose_name = 'Correo', max_length = 50)

	# Crear / Insertar / Agregar - POST

	# Revisar / Buscar - GET

	# Actualizar / Editar - PUT

	# Eliminar / Remover - DELETE
from django.db import models
from login.models import CustomUser

class CanvasModelManager(models.Manager):
    def for_user(self, user):
        return self.get_queryset().filter(user=user)

class CanvasModel(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    # Propuesta de valor
    value_proposition = models.TextField(blank=True, null=True)
    # Segmentos de clientes
    customer_segments = models.TextField(blank=True, null=True)
    # Canales
    channels = models.TextField(blank=True, null=True)
    # Relaciones con clientes
    customer_relationships = models.TextField(blank=True, null=True)
    # Fuentes de ingresos
    revenue_streams = models.TextField(blank=True, null=True)
    # Recursos clave
    key_resources = models.TextField(blank=True, null=True)
    # Actividades clave
    key_activities = models.TextField(blank=True, null=True)
    # Socios clave
    key_partners = models.TextField(blank=True, null=True)
    # Estructura de costos
    cost_structure = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relación con el usuario
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='canvas_models'
    )

    objects = CanvasModelManager()

    def __str__(self):
        return self.company_name



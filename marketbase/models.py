from django.db import models
from login.models import CustomUser

# Manager para Company
class CompanyBaseManager(models.Manager):
    def for_user(self, user):
        return self.get_queryset().filter(user=user)

class CompanyBase(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, unique=False)
    problem  = models.CharField(max_length=400, unique=False)
    target_age = models.CharField(max_length=3, unique=False)
    target_location = models.CharField(max_length=150, unique=False)
    target_interest = models.CharField(max_length=250, unique=False)
    differential_factor = models.CharField(max_length=250, unique=False)
    communication_type = models.CharField(max_length=15, unique=False) #Espero que sea un picklist: formal, casual, amigable, profesional
    call_actions = models.CharField(max_length=250, unique=False) #	¿Qué acción deseas que realicen tus clientes después de recibir tu mensaje (comprar, registrarse, contactar, etc.)?
    # Relación con el usuario
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='company_base'
    )

    objects = CompanyBaseManager()

    def __str__(self):
        return self.company_name
    


from django.db import models
from login.models import CustomUser

#########################
# Manager para Company
#########################
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

###############################
# Manager para CampaignMain
###############################
class CampaignMainManager(models.Manager):
    def for_user(self, user):
        return self.get_queryset().filter(user=user)

###############################
# Crear un modelo de Campaign
##############################
class CampaignMain(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=False)
    
    ##########################	
    # Relación con el usuario
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    objects = CampaignMainManager()

    def __str__(self):
        return self.id
    
######################
#######################
# Manager para Landing
######################
class LandingManager(models.Manager):
    def for_user(self, user):
        return self.get_queryset().filter(user=user)
    

# Modelo para Wireframes de Landings Pages
class Landing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=False)
    description = models.CharField(max_length=500, unique=False)
    call_action01 = models.CharField(max_length=300, unique=False)
    call_action02 = models.CharField(max_length=300, unique=False)
    call_action03 = models.CharField(max_length=300, unique=False)
    about_us = models.CharField(max_length=500, unique=False)
    beneficios_clave = models.CharField(max_length=500, unique=False)
    testimonials = models.CharField(max_length=500, unique=False)
    faqs = models.CharField(max_length=500, unique=False)
    wireframe_type = models.CharField(max_length=200, unique=False) #tipo_1, tipo_2, tipo_3

    ### Relación Con Campañas ###
    campaign = models.OneToOneField(
        'CampaignMain', 
        on_delete=models.CASCADE, 
        related_name='landing',  # acceso: campaign_instance.landing
        null=True, 
        blank=True
    )

    ##########################	
    # Relación con el usuario
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE
    )

    objects = LandingManager()

    def __str__(self):
        return self.title
        


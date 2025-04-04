from rest_framework import serializers
from .models import CompanyBase
from .models import Landing
from .models import CampaignMain




class CompanyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBase
        fields = '__all__'

class CampaignMainSerializer(serializers.ModelSerializer):
    ## Se agregó esto al agregar tabla Landing 1 a 1
    landing_id = serializers.SerializerMethodField()

    class Meta:
        model = CampaignMain
        fields = (
            'id',
            'name',
            'user',
            ## Se agregó esto al agregar tabla Landing 1 a 1
            'landing_id',
        )


    ## Se agregó esto al agregar tabla Landing 1 a 1
    def get_landing_id(self, obj):
        return getattr(obj.landing, 'id', None)

    def create(self, validated_data):
        user = self.context['request'].user

        # Sacar el campo 'user' si viene en validated_data (por precaución)
        validated_data.pop('user', None)

        campaign = CampaignMain.objects.create(user=user, **validated_data)

            
        ###############################################
        # Crear landing predeterminada para la campaña
        #       esta información la debe crear ChatGPT
        ###############################################
        Landing.objects.create(
            campaign=campaign,
            user=user,
            title="Título predeterminado",
            description="Descripción predeterminada",
            call_action01="Llamado a la acción 1",
            call_action02="Llamado a la acción 2",
            call_action03="Llamado a la acción 3",
            about_us="Sobre nosotros...",
            beneficios_clave="Beneficios clave",
            testimonials="Testimonios",
            faqs="Preguntas frecuentes",
            wireframe_type="tipo_1"
        )

        return campaign



class LandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landing
        fields = '__all__'


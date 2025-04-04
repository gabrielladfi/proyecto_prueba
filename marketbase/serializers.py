from rest_framework import serializers
from .models import CompanyBase
from .models import Landing
from .models import CampaignMain




class CompanyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBase
        fields = '__all__'


class CampaignMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignMain
        fields = '__all__'


class LandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landing
        fields = '__all__'


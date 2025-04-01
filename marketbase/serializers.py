from rest_framework import serializers
from .models import CompanyBase
from .models import Landing


class CompanyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBase
        fields = '__all__'


class LandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landing
        fields = '__all__'


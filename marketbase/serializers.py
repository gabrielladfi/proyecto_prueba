from rest_framework import serializers
from .models import CompanyBase

class CompanyBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBase
        fields = '__all__'

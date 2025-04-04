from django.urls import path
from .views import *

urlpatterns = [
        path('company_base/', CompanyBaseAPIView.as_view(), name='titulares-list-create'),
        path('company_base/<int:pk>/', CompanyBaseDetail.as_view(), name='titulares-detail'),
        path('landing/', LandingAPIView.as_view(), name='titulares-list-create'),
        path('landing/<int:pk>/', LandingDetail.as_view(), name='titulares-detail'),
        path('campaigns/', CampaignMainAPIView.as_view(), name='titulares-list-create'),
        path('campaigns/<int:pk>/', CampaignMainDetail.as_view(), name='titulares-detail'),
]
from django.urls import path
from .views import *

urlpatterns = [
        path('company_base/', CompanyBaseAPIView.as_view(), name='titulares-list-create'),
        path('company_base/<int:pk>/', CompanyBaseDetail.as_view(), name='titulares-detail'),
]
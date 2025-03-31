from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('list/', CanvasModelAPIView.as_view(), name='titulares-list-create'),
    path('list/<int:pk>/', CanvasModelDetail.as_view(), name='titulares-detail'),
]
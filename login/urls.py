from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/encrypted-login/', EncryptedLoginView.as_view(), name='encrypted_login'),
    path('api/create-user/', UserCreateView.as_view(), name='create-user'),
]
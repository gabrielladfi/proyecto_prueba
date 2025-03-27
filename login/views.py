from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserCreateSerializer
from .serializers import UserSerializer
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from drf_yasg.utils import swagger_auto_schema
import base64

@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(APIView):
    
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=UserCreateSerializer,
        operation_description="Endpoint para agendar una cita.",
        responses={201: "Paciente creado exitosamente", 400: "Error en los datos enviados"}
    )

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "Usuario creado exitosamente",
                    "user": {
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "country": user.country
                    }
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

###########
# Creación de usuario
###########

    


class EncryptedLoginView(APIView):
    secret_key = "FGa62cSP505X6AiQdJI3h2N8LBoXMNyB"

    permission_classes = [AllowAny]

    def decrypt_password(self, encrypted_password):
        try:
            # Decodificar la contraseña cifrada y separar IV y datos encriptados
            encrypted_data = base64.b64decode(encrypted_password)
            iv = encrypted_data[:AES.block_size]
            encrypted_password = encrypted_data[AES.block_size:]
            cipher = AES.new(self.secret_key.encode('utf-8'), AES.MODE_CBC, iv)
            decrypted_password = unpad(cipher.decrypt(encrypted_password), AES.block_size).decode('utf-8')
            return decrypted_password
        except Exception as e:
            print("Error al desencriptar la contraseña:", e)
            return None

    def post(self, request):
        email = request.data.get("email")
        encrypted_password = request.data.get("password")

        # Desencriptar la contraseña
        password = self.decrypt_password(encrypted_password)
        if password is None:
            return Response({"detail": "Error de desencriptación"}, status=status.HTTP_400_BAD_REQUEST)

        # Autenticar al usuario
        user = authenticate(email=email, password=password)
        if user is not None:
            # Generar token JWT
            custom_user = CustomUser.objects.get(email=email)
            serailized_user = UserSerializer(custom_user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_info': serailized_user.data
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
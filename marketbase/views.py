from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404
from .models import CompanyBase
from .serializers import CompanyBaseSerializer


class CompanyBaseAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        model_object = CompanyBase.objects.for_user(request.user)
        serializer = CompanyBaseSerializer(model_object, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanyBaseSerializer(data=request.data)
        if serializer.is_valid():
            #Asignación al usuario
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyBaseDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def get_object(self, pk, user):
        try:
            return CompanyBase.objects.for_user(user).get(id=pk)
        except CompanyBase.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        model_object = self.get_object(pk, request.user)
        serializer = CompanyBaseSerializer(model_object)
        return Response(serializer.data)

    def put(self, request, pk):
        model_object = self.get_object(pk, request.user)
        serializer = CompanyBaseSerializer(model_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        model_object = self.get_object(pk, request.user)
        model_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

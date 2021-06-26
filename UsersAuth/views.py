from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from UsersAuth.serializers import UserSerializer , LoginSerializers ,LogoutSerializer

from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import authentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate, login
from rest_framework import authentication
from rest_framework import exceptions

from .models import User
from django.http import JsonResponse
from django.contrib.auth import get_user_model, logout
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"Login":"Login Successfully", "status": status.HTTP_200_OK, "Token": token.key})






class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class =LogoutSerializer
    @action(methods=['POST'], detail=False)
    def logout(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)

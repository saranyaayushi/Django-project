from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from rest_framework.authtoken.models import Token
from .models import Medicine
from .serializers import MedicineSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class Signupuser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        confirm_password = serializer.validated_data.get('confirm_password')

        if password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already registered'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class Loginuser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class MedicineList(generics.ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticated]


class MedicineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateMedicine(generics.CreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticated]


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
        
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import (
    RegisterSerializer,
    VerifyPhoneSerializer,
    LoginSerializer,
    UserListSerializer
)
from .utils.sms import send_otp

otp_store = {}  # In-memory store; consider Redis for production

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone_number']
            otp = str(random.randint(1000, 9999))
            otp_store[phone] = otp
            send_otp(phone, otp)
            return Response({"message": "OTP sent to phone."})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyPhoneView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = VerifyPhoneSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone_number']
            otp = serializer.validated_data['otp']
            if otp_store.get(phone) == otp:
                user = User.objects.filter(phone_number=phone).first()
                if not user:
                    return Response({"error": "User not found"}, status=404)
                token, _ = Token.objects.get_or_create(user=user)
                del otp_store[phone]
                return Response({"token": token.key})
            return Response({"error": "Invalid OTP"}, status=400)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            return Response({"error": "Invalid credentials"}, status=400)
        return Response(serializer.errors, status=400)

class UserListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

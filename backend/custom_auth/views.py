from django.shortcuts import get_object_or_404, render
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import authenticate

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": str(RefreshToken.for_user(user).access_token)
        })

class LoginView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # Find the user by username
        user = get_object_or_404(User, username=username)

        if user is None:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT token
        token = str(RefreshToken.for_user(user).access_token)

        return Response({
            "message": "Login successful",
            "user": UserSerializer(user).data,
            "token": token
        })
        
class GetUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect


class UserAccountViewset(viewsets.ModelViewSet):
    queryset = models.UserAccount.objects.all()
    serializer_class = serializers.UserAccountSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            confirm_link = f"http://127.0.0.1:8000/user_accounts/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_staff=True
        user.is_superuser = True
        user.save()
        return redirect('http://localhost:3000/login')
    else:
        return redirect('http://localhost:3000/register')
    

class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)

# class UserLogoutView(APIView):
#     def get(self, request):
#         request.user.auth_token.delete()
#         logout(request)
#          # return redirect('login')
#         return Response({'success' : "logout successful"})
        
class UserLogoutView(APIView):
    def get(self, request):
        user = request.user
        
        # Check if user is authenticated
        if not user.is_authenticated:
            return Response({'error': 'User not authenticated'})
        
        # Attempt to delete the auth_token if it exists
        try:
            token = Token.objects.get(user=user)
            token.delete()
        except Token.DoesNotExist:
            logout(request)
            return Response({'error': 'Logout Successfull'})
        
        # Log the user out
        logout(request)
        return Response({'success': 'Logout successful'})
from rest_framework.response import Response
from rest_framework.decorators import api_view
from registration import serializers
from registration import models
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from registration import models
from rest_framework.views import APIView


class society_registration_view(generics.CreateAPIView):
    queryset = models.society.objects.all()
    serializer_class = serializers.SocietyRegistrationSerializer


class player_registration_view(generics.CreateAPIView):
    queryset = models.player.objects.all()
    serializer_class = serializers.PlayerRegistrationSerializer


class user_login(APIView):
	queryset = models.player.objects.all()
	serializer_class = serializers.UserLoginSerializer 

	def post(self, request):
		serializer = serializers.UserLoginSerializer(data=request.data)
		if serializer.is_valid():
			user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
			if not user:
				return Response({'error': 'Invalid credentials'})
			refresh = RefreshToken.for_user(user)
			return Response({
				        'refresh': str(refresh),
						'access': str(refresh.access_token),
							})
		return Response(serializer.error_messages)
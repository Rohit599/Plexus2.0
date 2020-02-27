from rest_framework.response import Response
from rest_framework.decorators import api_view
from registration.api import serializers
from registration import models
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken




@api_view(['POST',])
def player_registration_view(request):

	if request.method == 'POST':

		serializer = serializers.PlayerRegistrationSerializer(data=request.data)
		if serializer.is_valid(raise_exception=ValueError):
			serializer.create(validated_data=request.data)
			return Response(serializer.data)
		return Response(serializer.error_messages)




@api_view(['POST',])
def society_registration_view(request):

	if request.method == 'POST':

		serializer = serializers.SocietyRegistrationSerializer(data=request.data)
		if serializer.is_valid(raise_exception=ValueError):
			serializer.create(validated_data=request.data)
			return Response(serializer.data)
		return Response(serializer.error_messages)


@api_view(['POST',])
def player_login(request):

	if request.method == 'POST':

		serializer = serializers.UserLoginSerializer(data=request.data)
		if serializer.is_valid():
			if serializer.data['table'] == 0:
				table = models.player 
			else:
				table = models.society
			user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
			if not user:
				return Response({'error': 'Invalid credentials'})
			refresh = RefreshToken.for_user(user)
			return Response({
				        'refresh': str(refresh),
						'access': str(refresh.access_token),
    						})
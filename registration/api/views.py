from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from registration.api.serializers import PlayerRegistrationSerializer, SocietyRegistrationSerializer

@api_view(['POST',])
def player_registration_view(request):

	if request.method == 'POST':

		serializer = PlayerRegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			Player = serializer.save()
			data['response'] = "Registration Successful"
			data['name'] = Player.name
			data['email'] = Player.email
			data['admissionNo'] = Player.admissionNo
			data['contact'] = Player.contact
			data['college'] = Player.college
			data['password'] = Player.password
		else:
			data = serializer.errors
		return Response(data)


@api_view(['POST',])
def society_registration_view(request):

	if request.method == 'POST':

		serializer = SocietyRegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			Society = serializer.save()
			data['response'] = "Registration Successful"
			data['username'] = Society.username
			data['name'] = Society.name
			data['email'] = Society.email
			data['description'] = Society.description
			data['password'] = Society.password
		else:
			data = serializer.errors
		return Response(data)

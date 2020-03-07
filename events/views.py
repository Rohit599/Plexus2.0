from rest_framework.response import Response
from events import serializers
from rest_framework import generics
from events import models
from registration.models import society


# Create your views here.


class EventViewSet(viewsets.ModelViewSet):
	queryset = models.Event.objects.all()
	serializer_class = serializers.EventSerializer

	# def get_queryset(self):
	#     user = self.request.user.username
	#     return Event.objects.filter(society=user)

	def perform_create(self, serializer):
		new_society = society.objects.get(user=request.user)
		serializer.save(society=new_society)

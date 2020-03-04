from events.models import Event
from rest_framework import viewsets, permissions
from .serializers import EventSerializer
from registration.models import society

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = EventSerializer

    def get_queryset(self):
        return self.request.user.events.all()
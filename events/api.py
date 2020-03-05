from events.models import Event
from rest_framework import viewsets, permissions
from .serializers import EventSerializer
from registration.models import society
from .models import Event, Question, Score, Rule
from .serializers import QuestionSerializer, ScoreSerializer, RuleSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.all()


# class AnswerViewSet(viewsets.ModelViewSet):
#     queryset = Answers.objects.all()
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]

#     serializer_class = AnswerSerializer

#     def get_queryset(self):
#         return Answers.objects.all()


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = ScoreSerializer

    def get_queryset(self):
        return Score.objects.all()


class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = RuleSerializer

    def get_queryset(self):
        return Rule.objects.all()

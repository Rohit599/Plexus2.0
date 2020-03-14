from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from registration.models import society
from .models import Event, Question, Score, Rule
from .serializers import EventSerializer, QuestionSerializer, ScoreSerializer, RuleSerializer
from rest_framework.reverse import reverse


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        new_society = society.objects.get(user=self.request.user)
        serializer.save(society=new_society)

    def get_questions(self, obj):
        query = obj.Question.all().order_by('order')
        return QuestionSerializer(query, many=True, read_only=True).data


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        new_society = society.objects.get(user=self.request.user)
        serializer.save(society=new_society)

    def get_queryset(self):
        return Question.objects.filter(event=self.kwargs['event_pk'])


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    def get_queryset(self):
        return Score.objects.all()


class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

    def get_queryset(self):
        return Rule.objects.all()


class StartEvent(APIView):
    def get(self, request):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)


class EventDetails(APIView):
    def get(self, request, pk, format=None):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)


class QuestionsPlay(APIView):
    def get(self, request, *args, **kwargs):
        url_event = self.kwargs["pk"]
        # questions = Question.objects.filter(event=url_event).order_by("level")
        # serializer = QuestionSerializer(questions, many=True)
        # level_count = self.kwargs["level"]
        level_count = 1
        if level_count == 0:
            question = Question.objects.filter(event=url_event, level=1)
        else:
            level_count+=1
            question = Question.objects.filter(event=url_event, level=level_count)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        level = request.data.get("level")
        return Response(level)
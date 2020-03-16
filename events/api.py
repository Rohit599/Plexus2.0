from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from registration.models import society
from .models import Event, Question, Score, Rule
from .serializers import EventSerializer, QuestionSerializer, RuleSerializer


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


class RuleViewSet(viewsets.ModelViewSet):
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

    def perform_create(self, serializer):
        new_society = society.objects.get(user=self.request.user)
        serializer.save(society=new_society)


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
        event_url = self.kwargs["pk"]
        try:
            score_play = Score.objects.get(player=self.request.user, event=event_url)
        except KeyError:
            score_play = Score.objects.create(player=self.request.user, event=event_url)
        level = score_play.level
        question = Question.objects.get(event=event_url, level=level)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        event_url = self.kwargs["pk"]
        try:
            score_play = Score.objects.get(player=self.request.user, event=event_url)
        except KeyError:
            score_play = Score.objects.create(player=self.request.user, event=event_url)
        level = score_play.level
        answer = request.data["answer"]
        question = Question.objects.get(event=event_url, level=level)
        if answer == question.answer:
            score_play.level += 1
            return Response({"answer": "Correct"})
        else:
            return Response({"answer": "Inorrect"})

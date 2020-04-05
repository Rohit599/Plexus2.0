from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from registration.models import society
from .models import Event, Question, Score, Rule
from .serializers import EventSerializer, QuestionSerializer, RuleSerializer
from django.core.signing import Signer
signer = Signer()


class EventViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        new_society = society.objects.get(user=self.request.user)
        serializer.save(society=new_society)


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class RuleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Rule.objects.all()
    serializer_class = RuleSerializer
 

class StartEvent(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(serializer.data)


class EventDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        event = get_object_or_404(Event, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)


class QuestionsPlay(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        event_url = self.kwargs["pk"]
        player_id = self.request.user.player
        score_play, created = Score.objects.get_or_create(player=player_id, event=Event.objects.get(pk=event_url))
        level = score_play.level
        question = Question.objects.get(event=event_url, level=level)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        event_url = self.kwargs["pk"]
        score_play = Score.objects.get(player=self.request.user.player, event=event_url)
        level = score_play.level
        answer = request.data["answer"]
        question = Question.objects.get(event=event_url, level=level)
        # cor_answer = signer.unsign(question.answer)
        if answer == question.answer:
            score_play.level += 1
            score_play.score += question.correct_score
            score_play.save()
            return Response({"answer": "Correct"})
        else:
            score_play.score += question.incorrect_score
            score_play.save()
            return Response({"answer": "Incorrect"})

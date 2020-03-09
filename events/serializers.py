from rest_framework import serializers
from .models import Event, Question, Score, Rule


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'description', 'start_time', 'end_time',
                  'duration', 'total_ques', 'event_type', 'forum']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'

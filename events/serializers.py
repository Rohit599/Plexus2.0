from rest_framework import serializers
from .models import Event, Question, Score, Rule
import datetime


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('society','duration')

    def create(self, validated_data):
        datetimeFormat = '%Y-%m-%d %H:%M:%S%z'
        start = str(validated_data['start_time'])
        end = str(validated_data['end_time'])
        dura = datetime.datetime.strptime(start, datetimeFormat)\
                        - datetime.datetime.strptime(end, datetimeFormat)
        event_obj = Event.objects.create(duration=dura.seconds, **validated_data)
        event_obj.save()
        return event_obj


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('event',)


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'
        read_only_fields = ('event',)


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['event', 'player', 'score','level']

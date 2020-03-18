from rest_framework import serializers
from .models import Event, Question, Rule
from django.core.signing import Signer
signer = Signer()


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('society','duration')

    def create(self, validated_data):
        start = validated_data['start_time']
        end = validated_data['end_time']
        dura = end.date() - start.date()
        event_obj = Event.objects.create(duration=dura.days, **validated_data)
        event_obj.save()
        return event_obj


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('event',)

    def create(self, validated_data):
        encanswer = validated_data.pop('answer')
        enc = signer.sign(encanswer)
        question_obj = Question.objects.create(answer=enc, **validated_data)
        question_obj.save()
        return question_obj


class RuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'
        read_only_fields = ('event',)

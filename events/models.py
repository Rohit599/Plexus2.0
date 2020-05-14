from django.db import models
from tinymce import models as tinymce_models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.signing import Signer
signer = Signer()


class Event(models.Model):

    society = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField(
        help_text="Enter the starting date and time")
    end_time = models.DateTimeField(
        help_text="Enter the ending date and time")
    duration = models.IntegerField(
        help_text="time duration is in minutes")
    total_ques = models.IntegerField()
    forum = models.TextField()
    player_score = models.ManyToManyField(
        get_user_model(),
        through='Score',
        related_name='event_num')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def correct_dates(self):
        if (self.end_time) < (self.start_time):
            raise ValidationError(
                "End date should be greater than start date.")


class Question(models.Model):

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='questions',
        blank=True,
        null=True)
    question = models.TextField()
    answer = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    html = tinymce_models.HTMLField(null=True)
    correct_score = models.IntegerField()
    incorrect_score = models.IntegerField()
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def encanswer(self):
        return signer.sign(self.answer)


class Score(models.Model):

    player = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='player_score')
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='event_score')
    score = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rule(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rules = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

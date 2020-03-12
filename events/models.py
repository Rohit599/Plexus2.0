from django.db import models
from registration.models import society, player
from tinymce import models as tinymce_models
from django.core.signing import Signer
signer = Signer()

class Event(models.Model):

    society = models.ForeignKey(society, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField(help_text="time duration is in minutes")
    total_ques = models.IntegerField()
    event_type = models.IntegerField()
    forum = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name_plural = "events"


class Question(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE,
                              related_name='questions', blank=True, null=True)
    question = models.TextField()
    answer = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    html = tinymce_models.HTMLField(null=True)
    score = models.IntegerField()
    answer = models.CharField(max_length=200)
    incorrect_score = models.IntegerField(null=True)
    event_type = models.CharField(max_length=10)
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.question)

    def answer(self):
        return (signer.sign(self.answer.__self__))

    class Meta:
        verbose_name_plural = "questions"


class Score(models.Model):

    player = models.ForeignKey(player, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    score = models.IntegerField()
    level = models.IntegerField()
    counter = models.IntegerField()
    logged_on = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.player)

    class Meta:
        verbose_name_plural = "scores"


class Rule(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rules = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.rules)

    class Meta:
        verbose_name_plural = "rules"

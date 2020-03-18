from django.db import models
from tinymce import models as tinymce_models
from django.core.signing import Signer
signer = Signer()


class Event(models.Model):

    society = models.ForeignKey('registration.society', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField(help_text="time duration is in minutes")
    total_ques = models.IntegerField()
    forum = models.TextField()
    player_score = models.ManyToManyField('registration.player', through='events.Score', related_name='event_num')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        verbose_name_plural = "events"


class Question(models.Model):

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    question = models.TextField()
    answer = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    html = tinymce_models.HTMLField(null=True)
    correct_score = models.IntegerField()
    answer = models.CharField(max_length=200)
    incorrect_score = models.IntegerField()
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.question)

    # def answer(self):
    #     return (signer.sign(self.answer.__self__))

    class Meta:
        verbose_name_plural = "questions"


class Score(models.Model):

    player = models.ForeignKey('registration.player', on_delete=models.CASCADE, related_name='player_score')
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, related_name='event_score')
    score = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rule(models.Model):

    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    rules = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.rules)

    class Meta:
        verbose_name_plural = "rules"

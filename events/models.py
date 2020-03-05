from django.db import models
from django.contrib.auth.models import User
from registration.models import society, player


class Event(models.Model):
    eventName = models.CharField(max_length=250)
    eventCode = models.IntegerField(null=True)
    eventDes = models.TextField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    duration = models.IntegerField(
        help_text="time duration of events in minutes")
    totalQues = models.IntegerField()
    societyId = models.ForeignKey(society, on_delete=models.CASCADE, null=True)
    Type = models.IntegerField()
    status = models.IntegerField()
    forum = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.eventName)

    class Meta:
        verbose_name_plural = "events"


class Question(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    question = models.TextField()
    image = models.ImageField()
    html = models.TextField()
    score = models.IntegerField()
    answer = models.CharField(max_length=200)
    incorrect_scr = models.IntegerField()
    Type = models.CharField(max_length=10)
    level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.question)

    class Meta:
        verbose_name_plural = "questions"


# class Answers(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     score = models.IntegerField()
#     answer = models.CharField(max_length=200)
#     incorrect_scr = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return "%s" % (self.answer)

#     class Meta:
#         verbose_name_plural = "answers"


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    score = models.IntegerField()
    level = models.IntegerField()
    counter = models.IntegerField()
    logged_on = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % (self.username)

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

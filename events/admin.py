from django.contrib import admin
from events.models import Event, Question, Answers, Score, Rule


# Register your models here.

admin.site.register(Event)
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Score)
admin.site.register(Rule)
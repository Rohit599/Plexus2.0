from django.contrib import admin
from events.models import Event, Question, Score, Rule


# Register your models here.

admin.site.register(Event)
admin.site.register(Score)
admin.site.register(Rule)
admin.site.register(Question)

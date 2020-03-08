from django.contrib import admin
from events.models import Event, Question, Score, Rule


# Register your models here.

admin.site.register(Event)
# admin.site.register(Question)
admin.site.register(Score)
admin.site.register(Rule)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['event', 'question', 'image', 'html', 'score', 'answer', 'incorrect_scr', 'Type', 'level', 'created_at', 'updated_at']
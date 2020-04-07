from django.contrib import admin
from events.models import Event, Question, Score, Rule


# Register your models here.

admin.site.register(Event)
admin.site.register(Score)
admin.site.register(Rule)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'event',
        'question',
        'image',
        'html',
        'correct_score',
        'answer',
        'incorrect_score',
        'level',
        'created_at',
        'updated_at']

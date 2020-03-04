from django.contrib import admin
from registration.models import player, society
from events.models import Event


# Register your models here.

admin.site.register(player)
admin.site.register(society)

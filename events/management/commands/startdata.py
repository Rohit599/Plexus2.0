from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Creating user groups"

    def handle(self, *attrs, **options):
        _, created = Group.objects.get_or_create(name='Player')
        _, created = Group.objects.get_or_create(name='Society')
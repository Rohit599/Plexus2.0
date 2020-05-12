from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class player(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True)

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    admissionNo = models.CharField(max_length=13)
    contact_regex = RegexValidator(
        regex=r'^[6-9]\d{9}$',
        message="Enter a valid 10 digit phone number")
    contact = models.CharField(validators=[contact_regex], max_length=10)
    college = models.CharField(max_length=50)
    player_event = models.ManyToManyField(
        'events.Event',
        through="events.Score",
        related_name='player_info')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # avatar = models.ImageField(upload_to='avatars', blank='True')
    # optional for the user


class society(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='events')

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    privilege = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

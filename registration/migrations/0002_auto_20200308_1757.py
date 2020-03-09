# Generated by Django 3.0.3 on 2020-03-08 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='society',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='events', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
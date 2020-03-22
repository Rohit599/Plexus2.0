# Generated by Django 3.0.3 on 2020-03-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200319_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(help_text='Enter the ending date and time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(help_text='Enter the starting date and time'),
        ),
    ]
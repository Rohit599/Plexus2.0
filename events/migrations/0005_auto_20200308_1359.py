# Generated by Django 3.0.3 on 2020-03-08 08:29

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20200308_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=tinymce.models.HTMLField(),
        ),
    ]

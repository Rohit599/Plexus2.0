# Generated by Django 3.0.3 on 2020-03-18 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_score', to='registration.player'),
        ),
        migrations.AddField(
            model_name='rule',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AddField(
            model_name='question',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='events.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='player_score',
            field=models.ManyToManyField(related_name='event_num', through='events.Score', to='registration.player'),
        ),
        migrations.AddField(
            model_name='event',
            name='society',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.society'),
        ),
    ]

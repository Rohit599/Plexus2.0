from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0002_auto_20200308_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('duration', models.IntegerField(help_text='time duration is in minutes')),
                ('total_ques', models.IntegerField()),
                ('forum', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('html', tinymce.models.HTMLField(null=True)),
                ('correct_score', models.IntegerField()),
                ('answer', fernet_fields.fields.EncryptedTextField()),
                ('incorrect_score', models.IntegerField()),
                ('level', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'questions',
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('level', models.IntegerField()),
                ('counter', models.IntegerField()),
                ('logged_on', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.player')),
            ],
            options={
                'verbose_name_plural': 'scores',
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rules', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),

            ],
            options={
                'verbose_name_plural': 'rules',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_score', to='events.Event')),
            ],
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('html', tinymce.models.HTMLField()),
                ('score', models.IntegerField()),
                ('answer', models.CharField(max_length=200)),
                ('incorrect_score', models.IntegerField()),
                ('event_type', models.CharField(max_length=10)),
                ('level', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='events.Event')),
            ],
            options={
                'verbose_name_plural': 'questions',
            },
        ),
    ]

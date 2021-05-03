# Generated by Django 3.2 on 2021-05-03 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mumble',
            fields=[
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('vote_rank', models.IntegerField(blank=True, default=0, null=True)),
                ('comment_count', models.IntegerField(blank=True, default=0, null=True)),
                ('share_count', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.mumble')),
                ('remumble', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='remumbles', to='feed.mumble')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='MumbleVote',
            fields=[
                ('value', models.CharField(choices=[('upvote', 'upvote'), ('downvote', 'downvote')], max_length=20)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('mumble', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.mumble')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mumble',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='mumble_user', through='feed.MumbleVote', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 2.2.3 on 2019-09-17 20:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0003_auto_20190918_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followed_user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followed_users',
            field=models.ManyToManyField(default=None, related_name='followed_user', to=settings.AUTH_USER_MODEL, verbose_name='Followed users'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(default=None, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='Followers'),
        ),
    ]

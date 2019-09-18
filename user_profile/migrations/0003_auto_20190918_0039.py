# Generated by Django 2.2.3 on 2019-09-17 19:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0003_auto_20190918_0039'),
        ('user_profile', '0002_userprofile_is_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followed_user',
            field=models.ManyToManyField(default=None, related_name='followed_user', to=settings.AUTH_USER_MODEL, verbose_name='Followed user'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subscribed_tags',
            field=models.ManyToManyField(default=None, related_name='subscribed_tags', to='post.Tags', verbose_name='Subscribed Tags'),
        ),
    ]

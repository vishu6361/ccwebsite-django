# Generated by Django 2.2.3 on 2019-09-17 21:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_auto_20190918_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followed_users',
            field=models.ManyToManyField(blank=True, default=None, related_name='followed_user', to=settings.AUTH_USER_MODEL, verbose_name='Followed users'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, default=None, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='Followers'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='subscribed_tags',
            field=models.ManyToManyField(blank=True, default=None, related_name='subscribed_tags', to='post.Tags', verbose_name='Subscribed Tags'),
        ),
    ]
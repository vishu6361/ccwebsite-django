# Generated by Django 2.2.3 on 2019-09-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_userprofile_is_sound_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_password_set',
            field=models.BooleanField(default=False),
        ),
    ]
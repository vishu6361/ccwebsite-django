# Generated by Django 2.2.3 on 2019-09-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]

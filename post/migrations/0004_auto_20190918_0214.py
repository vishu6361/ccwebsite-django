# Generated by Django 2.2.3 on 2019-09-17 20:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20190918_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_on_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 17, 20, 44, 6, 550933, tzinfo=utc)),
        ),
    ]

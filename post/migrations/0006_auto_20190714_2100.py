# Generated by Django 2.1.5 on 2019-07-14 15:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20190714_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_on_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 14, 15, 30, 27, 654161, tzinfo=utc)),
        ),
    ]

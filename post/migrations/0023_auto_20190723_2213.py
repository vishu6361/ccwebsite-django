# Generated by Django 2.2.3 on 2019-07-23 16:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_auto_20190723_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='post_content',
        ),
        migrations.AlterField(
            model_name='post',
            name='post_on_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 23, 16, 43, 20, 247159, tzinfo=utc)),
        ),
    ]

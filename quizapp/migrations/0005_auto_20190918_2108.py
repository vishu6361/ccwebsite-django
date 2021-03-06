# Generated by Django 2.2.3 on 2019-09-18 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_currentquiz_sel_ans'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='neg_marks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='currentquiz',
            name='contrib',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userquizresult',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizapp.Quiz'),
        ),
        migrations.AlterField(
            model_name='userquizresult',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]

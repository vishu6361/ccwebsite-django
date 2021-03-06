# Generated by Django 2.2.3 on 2019-09-16 20:53

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Tag Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Tag Description')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Post Title')),
                ('post_content', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Post Content')),
                ('is_pinned', models.BooleanField(default=False)),
                ('draft', models.BooleanField(default=False)),
                ('post_on_date', models.DateField(default=datetime.datetime(2019, 9, 16, 20, 53, 36, 335289, tzinfo=utc))),
                ('published', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('updated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('slug', models.SlugField(blank=True, default='')),
                ('verify_status', models.IntegerField(default=-1, verbose_name='Is verified')),
                ('deleted', models.BooleanField(default=False)),
                ('is_scheduled', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='post.Tags', verbose_name='Post Tags')),
            ],
        ),
    ]

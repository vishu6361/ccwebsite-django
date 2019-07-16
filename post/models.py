from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
# Create your models here.

# Model manager
# https://www.youtube.com/watch?v=BrbaKmyTOMc&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy&index=36


class PostManager(models.Manager):
    # Overriding all() model manager
    def all(self, native_user=None, draft=False, *args, **kwargs):
        if native_user is None:
            if not draft:
                return super(PostManager, self).filter(draft=False).filter(post_on_date__lte=timezone.now()).order_by(
                    '-published')
            return super(PostManager, self).filter(draft=True).filter(post_on_date__lte=timezone.now()).order_by(
                    '-published')
        else:
            if not draft:
                return super(PostManager, self).filter(draft=False).filter(post_on_date__lte=timezone.now()).filter(
                    author=native_user).order_by('-published')
            return super(PostManager, self).filter(draft=True).filter(post_on_date__lte=timezone.now()).filter(
                    author=native_user).order_by('-published')


class Tags(models.Model):
    name = models.CharField(max_length=255, verbose_name='Tag Name')
    description = models.TextField(blank=True, null=True, verbose_name='Tag Description')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Post Title')
    content = RichTextUploadingField(blank=True, null=True, verbose_name='Post Content')

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )

    # To create Draft and publish post on specific day.
    draft = models.BooleanField(default=False)
    post_on_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())

    published = models.DateTimeField(default=datetime.now, blank=True)
    tags = models.ManyToManyField(Tags, verbose_name='Post Tags', blank=True)
    slug = models.SlugField(default='', blank=True)

    # Initialising post manager
    objects = PostManager()

    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        return '%s' % self.title

    @property
    def get_content_type(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return content_type



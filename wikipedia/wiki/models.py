from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class forum_post(models.Model):
    semester = (
        ('I', 'I Semestr'),
        ('II', 'II Semestr'),
        ('III', 'III Semestr'),
        ('IV', 'IV Semestr'),
        ('V', 'V Semestr'),
        ('VI', 'VI Semestr'),
        ('VII', 'VII Semestr')
    )
    title = models.CharField(max_length=255, blank=False)
    semestr = models.CharField(blank=False, choices=semester, max_length=15)
    category = models.CharField(default='#elektro', max_length=50)
    text = models.TextField(default='Write your post here!', verbose_name='Post text:')
    creation_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(default=timezone.now)
    text = models.TextField(blank=False)
    edit_date = models.DateTimeField(default=timezone.now)
    post_reference = models.ForeignKey(forum_post, default=None, on_delete=models.CASCADE)


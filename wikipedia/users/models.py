from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


# Create your models here.
class Profile(models.Model):
    semester = (
        ('I', 'I Semestr'),
        ('II', 'II Semestr'),
        ('III', 'III Semestr'),
        ('IV', 'IV Semestr'),
        ('V', 'V Semestr'),
        ('VI', 'VI Semestr'),
        ('VII', 'VII Semestr')
    )
    plec = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('U', 'Undefined')
    )
    groups = (
        ('Admin', 'Admin'),
        ('Mod', 'Moderator'),
        ('User', 'User'),
        ('Bann', 'Banned')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='This is default Bio!', blank=True)
    Name = models.CharField(max_length=50, help_text=mark_safe("<ul><li>Name should not contain any numbers or special"
                                                               " chars</li></ul>"), blank=True)
    Age = models.IntegerField(blank=True, null=True)
    surname = models.CharField(max_length=70, blank=True)
    semestr = models.CharField(choices=semester, max_length=3, blank=True)
    kierunek = models.CharField(max_length=20, blank=True)
    gender = models.CharField(choices=plec, default='U', max_length=1, blank=True)
    group = models.CharField(choices=groups, default='User', max_length=5, blank=True)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
class ProfilePrivacy(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    hidden_Age = models.BooleanField(default=False, help_text=mark_safe('<p>Hide your age: </p>'))

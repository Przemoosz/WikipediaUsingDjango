# Generated by Django 3.2.8 on 2021-10-27 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='This is default Bio!')),
                ('Name', models.TextField(max_length=50)),
                ('surname', models.TextField(max_length=70)),
                ('semestr', models.CharField(choices=[('I', 'I Semestr'), ('II', 'II Semestr'), ('III', 'III Semestr'), ('IV', 'IV Semestr'), ('V', 'V Semestr'), ('VI', 'VI Semestr'), ('VII', 'VII Semestr')], max_length=3)),
                ('kierunek', models.TextField(max_length=20)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Undefined')], default='U', max_length=1)),
                ('group', models.CharField(choices=[('Admin', 'Admin'), ('Mod', 'Moderator'), ('User', 'User'), ('Bann', 'Banned')], default='User', max_length=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-14 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_comments_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='post',
            new_name='post_reference',
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_rename_post_comments_post_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum_post',
            name='text',
            field=models.TextField(default='Write your post here!', verbose_name='Post text:'),
        ),
    ]
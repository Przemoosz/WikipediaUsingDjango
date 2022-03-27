from django.contrib import admin
from .models import forum_post,Comments
# Register your models here.
admin.site.register(forum_post)
admin.site.register(Comments)
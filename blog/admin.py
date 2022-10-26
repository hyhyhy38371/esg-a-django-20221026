from django.contrib import admin

from blog.models import Post #책에서는 from .model이었음

admin.site.register(Post)
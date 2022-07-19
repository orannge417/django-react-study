from django.contrib import admin
from .models import Post

# Postモデルを管理画面で操作できるように
admin.site.register(Post)
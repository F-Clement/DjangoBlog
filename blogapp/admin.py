from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# @admin.register(Post)
# class PostAdmin(SummernoteModelAdmin):

#     summernote_fields = ('text')


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Post, PostAdmin)

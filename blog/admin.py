from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','subject','approved')
    list_filter = ('approved','name')


admin.site.register(BlogPost, PostAdmin)
admin.site.register(Comment,CommentAdmin)


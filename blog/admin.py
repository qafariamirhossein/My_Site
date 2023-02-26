from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_date')


admin.site.register(BlogPost, PostAdmin)

from django.contrib import admin
from .models import *
from .forms import *
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','subject','approved')
    list_filter = ('approved','name')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Comment,CommentAdmin)
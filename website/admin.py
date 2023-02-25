from django.contrib import admin
from .models import *
from .forms import *
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Contact,ContactAdmin)

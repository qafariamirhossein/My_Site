from django.contrib import admin
from .models import *
from .forms import *
from django_summernote.admin import SummernoteModelAdmin


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_date')

admin.site.register(Contact,ContactAdmin)

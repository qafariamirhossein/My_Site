from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.urls import reverse

        
class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)



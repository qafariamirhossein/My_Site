from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class BlogPost(models.Model):
    image = models.ImageField(upload_to ='website/',default='website/default.jpg')
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=False)
    tags = TaggableManager()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.title
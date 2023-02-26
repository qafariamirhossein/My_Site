from django.db import models
from taggit.managers import TaggableManager

class BlogPost(models.Model):
    image = models.ImageField(upload_to ='website/',default='website/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=False)
    #category = models.ManyToManyField()
    tags = TaggableManager()
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
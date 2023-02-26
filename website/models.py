from django.db import models
from taggit.managers import TaggableManager



class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to ='website/',default='website/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = TaggableManager()
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

        
class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)



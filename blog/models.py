from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
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

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.title} '{self.id}'"


    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})

class Comment(models.Model):
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    subject = models.CharField(max_length=225)
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)



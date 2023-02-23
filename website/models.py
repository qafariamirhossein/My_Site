from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to ='uploads/',default='image/banner-item-03.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField(default=False)
    #category = models.ManyToManyField()
    #tag
    author = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now_add=True)

    #comment
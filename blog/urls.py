from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('blog/',blog_view,name='mainblog'),
]

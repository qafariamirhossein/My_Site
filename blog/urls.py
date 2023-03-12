from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('blog/',blog_view,name='mainblog'),
    path('<int:pid>',postdetails_view,name='post-details'),
    path('category/<str:cat_name>',blog_category,name='category'),
    path('tag/<str:tag_name>',blog_tag,name='tag'),
    path('writer/<str:author_name>',blog_author,name='author'),

]

from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('',index_view,name='index'),
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact'),
    path('category/<str:cat_name>',web_category,name='category'),
    path('tag/<str:tag_name>',web_tag,name='tag'),
    path('writer/<str:writer_name>',web_writer,name='writer'),
    path('<int:pid>',postdetails_view,name='post-details'),

]

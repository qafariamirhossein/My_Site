from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('',index_view,name='index'),
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact'),
    path('post-details/<int:pid>',postdetails_view,name='post-details'),

]

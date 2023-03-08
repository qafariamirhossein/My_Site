from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup',signup_view,name='signup'),
    path('signin',signin_view,name='signin'),
    path('logout',logout_view,name='logout'),
    path('password_reset',password_reset_view,name='password_reset'),
]

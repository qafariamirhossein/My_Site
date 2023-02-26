from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *


def blog_view(request):
    blogPosts = BlogPost.objects.all()
    context = {'blogPosts':blogPosts}
    return render(request,'blog.html',context)
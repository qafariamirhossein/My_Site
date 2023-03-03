from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from django.core.paginator import Paginator

def blog_view(request):
    blogPosts = BlogPost.objects.all()
    paginator = Paginator(blogPosts, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'page_obj': page_obj})





    context = {'blogPosts':blogPosts}
    return render(request,'blog.html',context)
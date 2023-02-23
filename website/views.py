from django.shortcuts import render
from .models import *
# Create your views here.

def index_view(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'index.html',context)
    
def about_view(request):
    return render(request,'about.html')
    
def contact_view(request):
    return render(request,'contact.html')
    
def blog_view(request):
    return render(request,'blog.html')

def postdetails_view(request):
    return render(request,'post-details.html')
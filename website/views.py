from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from blog.views import*
from blog.models import*
from .forms import *
# Create your views here.

def index_view(request):
    posts = Post.objects.all()
    blogP = BlogPost.objects.all()
    context = {'posts':posts,'blogP':blogP}
    return render(request,'index.html',context)
    
def about_view(request):
    return render(request,'about.html')
    
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'thanks your ticket sent successfuly')
        else:
            messages.add_message(request,messages.ERROR,'your ticket didnt sent successfuly')

    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})
    



def postdetails_view(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'thanks your comment sent successfuly')
        else:
            messages.add_message(request,messages.ERROR,'oops your ticket didnt sent successfuly')

    
    form = CommentForm
    posts = Post.objects.all()
    post = get_object_or_404(posts,pk=pid)
    context = {'post':post,'form':form}
    return render(request,'post-details.html',context)

def web_category(request,cat_name):
    posts = Post.objects.all()
    posts = Post.objects.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'index.html',context)


def web_tag(request,tag_name):
    posts = Post.objects.all()
    posts = Post.objects.filter(tags__name=tag_name)
    context = {'posts':posts}
    return render(request,'index.html',context)

def web_writer(request,writer_name):
    posts = Post.objects.all()
    posts = Post.objects.filter(writer = writer_name)
    context = {'posts':posts}
    return render(request,'index.html',context)
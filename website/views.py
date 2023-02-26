from django.shortcuts import render
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
    



def postdetails_view(request):
    return render(request,'post-details.html')
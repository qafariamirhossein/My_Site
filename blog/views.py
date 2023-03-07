from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.core.paginator import Paginator

def blog_view(request):
    blogPosts = BlogPost.objects.all()
    paginator = Paginator(blogPosts, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'page_obj': page_obj})


def postdetails_view(request,pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'thanks your comment sent successfuly')
        else:
            messages.add_message(request,messages.ERROR,'ticket didnt sent ')

    
    form = CommentForm
    posts = BlogPost.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    context = {'post':post,'form':form}
    return render(request,'post-details.html',context)
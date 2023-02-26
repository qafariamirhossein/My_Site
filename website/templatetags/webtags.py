from django import template
from website.models import Post
from blog.models import BlogPost
register = template.Library()


@register.inclusion_tag('recent-posts.html')
def recentposts():
    posts = BlogPost.objects.all().order_by('-published_date')[:3]
    return {'posts':posts}
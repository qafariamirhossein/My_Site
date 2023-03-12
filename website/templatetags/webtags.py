from django import template
from blog.models import Post
register = template.Library()


@register.inclusion_tag('recent-posts.html')
def recentposts():
    posts = Post.objects.all().order_by('-published_date')[:3]
    return {'posts':posts}
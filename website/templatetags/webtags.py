from django import template
from blog.models import *
register = template.Library()


@register.inclusion_tag('recent-posts.html')
def recentposts():
    posts = Post.objects.all().order_by('-published_date')[:3]
    return {'posts':posts}


@register.inclusion_tag('categories.html')
def postcategories():
    posts = Post.objects.all()
    categories = Category.objects.all()
    cat_dict = {}
    
    for name in categories :
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}
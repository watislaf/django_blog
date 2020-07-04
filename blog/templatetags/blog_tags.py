from django import template
from ..models import Post

register = template.Library()

@register.simple_tag()
def total_posts(posts):  # name of tag
    return Post.published.count()

# Возвращает html latest в который был включён latest_posts
@register.inclusion_tag('blog/post/latest.html')
def show_latest_posts(count = 2):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

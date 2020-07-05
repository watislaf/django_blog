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

from django.utils.safestring import mark_safe
import markdown

@register.filter(name = 'markdown') # другое название тега. Хоть он тут ..._format но будет называться именно markdown
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

from django import template
from ..models import Post
from ..models import User

register = template.Library()

@register.simple_tag()
def total_posts(request):  # name of tag
    if request.user.is_authenticated:
        return User.objects.get(username = request.user).blog_posts.count()

@register.simple_tag()
def total_comments(request):  # name of tag
    if request.user.is_authenticated:
        return User.objects.get(username = request.user).comments.count()

# Возвращает html latest в который был включён latest_posts
@register.inclusion_tag('blog/post/latest.html')
def show_latest_posts(count = 2):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

from django.utils.safestring import mark_safe
import markdown

@register.filter(name = 'markdown')  # другое название тега. Хоть он тут ..._format но будет называться именно markdown
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

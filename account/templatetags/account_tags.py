from django import template

from django.contrib.auth.models import User

register = template.Library()

# Свой тег с использованием if else !
@register.simple_tag(takes_context = True)
def get_user_perm(context, request):
    # print(User.objects.get(email = request.POST['email']).blog_posts.count() != 0)
    print(request)
    return

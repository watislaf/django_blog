from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from .models import Post, Comment

from django.contrib.auth.decorators import login_required

def post_list(request):
    print('OKOKOOKKOKO')
    object_list = Post.published.all()
    # забрать все опубликованные обьекты

    paginator = Paginator(object_list, 2)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page': posts,
                   'posts': posts})
    # теперь у list есть поле posts

from django.views.generic import ListView

class PostListView(ListView):
    # помимо обычной функции мы можем использовать класс ListView который предоставит нам такой же функционл
    # с пагинацией
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post,
                             status = 'published',
                             publish__year = year,
                             publish__month = month,
                             publish__day = day)
    # List of active comments for this post
    comments = post.comments
    new_comment = None
    if request.method == 'POST':
        # A comment was posted, получить информациб из запроса
        comment_form = CommentForm(data = request.POST)
        if comment_form.is_valid() and \
                comments.filter(author = request.user).count() == 0 or not \
                comment_form.data['body'] == comments.filter(author = request.user).last().body:
            # Копирование без сохранения
            new_comment = comment_form.save(commit = False)
            # Меняем так свои параметры

            new_comment.post = post
            new_comment.author = request.user
            # Сохранение в database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # 404 или обьект с полями
    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})
    # теперь у detail есть поле post, из которого можно брать информацию

from .forms import EmailPostForm, CommentForm

from django.core.mail import send_mail

def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id = post_id, status = 'published')
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        # создаём форму на основе POST
        if form.is_valid():  # . You can see a list of validation errors by accessing form.errors
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'vladkozulin@mail.ru',
                      [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})

# from django.core.mail import send_mail
# send_mail('Django mail', 'This e-mail was sent with Django.', 'vladkozulin@mail.ru',
#          ['vladkozulin@mail.ru'], fail_silently=False)

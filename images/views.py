from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

from urllib import request

from account.forms import ImgUrl

@login_required
def image_create(request2):
    if request2.method == 'POST':
        # form is sent
        form = ImageCreateForm(data = request2.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit = False)
            # assign current user to the item
            new_item.user = request2.user

            new_item.save()
            messages.success(request2, 'Image added successfully')
            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data = request2.GET)
        url = request2.GET['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        try:
            opened = request.urlopen(url)
        except BaseException:
            return redirect('/account/?error=invalid')
        print(opened.__dict__)
        if extension not in valid_extensions:
            return redirect('/account/?error=neto')

    return render(request2,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})

from django.shortcuts import get_object_or_404
from .models import Image

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id = id, slug = slug)
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image})

from django.http import JsonResponse
from django.views.decorators.http import require_POST

@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id = image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'error'})

from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger

@login_required
def image_list(request):
    if request.method == 'POST' and not request.is_ajax():
        form = ImgUrl(request.POST)
        if not form.is_valid():
            messages.error(request, 'invalid url')
        else:
            return redirect(f'/images/create/?url={form.cleaned_data["image_url"]}&title=default')
    try:
        if request.GET['error'] == 'invalid':
            messages.error(request, 'invalid url')
        if request.GET['error'] == 'neto':
            messages.error(request, 'invalid format')
    except BaseException:
        pass
    form = ImgUrl()

    images = Image.objects.all()
    paginator = Paginator(images, 5)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range
            # return an empty page
            return HttpResponse('')
        # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'images/image/list_ajax.html',
                      {'section': 'images', 'images': images,
                       'form': form})
    return render(request,
                  'images/image/list.html',
                  {'section': 'images', 'images': images,
                   'form': form})

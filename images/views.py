from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

from urllib import request

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

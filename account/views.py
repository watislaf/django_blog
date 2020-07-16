from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm, ImgUrl
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance = request.user,
                                 data = request.POST)
        profile_form = ProfileEditForm(instance = request.user.profile,
                                       data = request.POST,
                                       files = request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        else:
            messages.error(request, 'unvalid form')
        if request.FILES.get('ava'):
            if request.user.profile.photo.name != '/users/no_photo.png':
                print(request.user.profile.photo.name)
                request.user.profile.photo.delete()

            request.user.profile.photo.save('.png', request.FILES.get('ava'))
            messages.success(request, 'Profile updated successfully')
            # request.user.profile.photo
    else:
        user_form = UserEditForm(instance = request.user)
        profile_form = ProfileEditForm(instance = request.user.profile)

    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            if User.objects.all().filter(email = user_form['email'].value()).count() != 0:
                messages.error(request, 'sorry email is already used')
            else:
                new_user = user_form.save(commit = False)
                # Set the chosen password
                new_user.set_password(
                    user_form.cleaned_data['password'])  # make hashing
                # Save the User object
                # Create the user profile
                new_user.save()
                Profile.objects.create(user = new_user)
                return render(request,
                              'account/register_done.html',
                              {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})

def user_login(request):
    # это является примером работы, в джанго давно есть готовый механизм
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return HttpResponse('Invalid login')

        cd = form.cleaned_data
        user = authenticate(request,
                            username = cd['username'],  # проверяет на существование и если такого нет
                            password = cd['password'])  # то возвращает none
        if user is None:
            return HttpResponse('Disabled account')

        if user.is_active:
            login(request, user)  # логирует в текущей сессии
            return HttpResponse('Authenticated successfully')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

@login_required
def user_list(request):
    users = User.objects.filter(is_active = True)
    return render(request,
                  'account/user/list.html',
                  {'section': 'people',
                   'users': users})

@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
                             username = username,
                             is_active = True)
    return render(request,
                  'account/user/detail.html',
                  {'section': 'people',
                   'user': user})

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Contact

@require_POST
@login_required
def user_follow(request):
    print('lol')
    if not request.is_ajax():
        return JsonResponse({'status': 'error'})

    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id = user_id)
            if action == 'follow':
                Contact.objects.get_or_create(
                    user_from = request.user,
                    user_to = user)
            else:
                Contact.objects.filter(user_from = request.user,
                                       user_to = user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})

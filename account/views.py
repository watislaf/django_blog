from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        messages.success(request, 'Profile registered successfully')
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
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

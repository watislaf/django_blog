from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

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
    return render(request,  'account/login.html', {'form': form})

from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})

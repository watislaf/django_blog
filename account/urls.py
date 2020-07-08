from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'account'
urlpatterns = [
    # post views
    # path('login/', views.user_login, name = 'login'),  # possible login view
    path('login/', auth_views.LoginView.as_view(), name = 'login2'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('', views.dashboard, name = 'dashboard'),
    path('edit/', views.edit, name = 'edit'),
    # register url
    path('register/', views.register, name = 'register'),

    # change password urls
    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             success_url = reverse_lazy('account:password_change_done')),
         name = 'password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name = 'password_change_done'),
    # reset password urls
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             success_url = reverse_lazy('account:password_reset_done')),
         name = 'password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             success_url = reverse_lazy('account:password_reset_complete')
         ),
         name = 'password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name = 'password_reset_complete'),
]

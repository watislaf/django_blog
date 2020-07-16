from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth',)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)


class ImgUrl(forms.Form):
    image_url = forms.URLField()


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label = 'Password',
                               widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repeat password',
                                widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

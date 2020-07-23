from django import forms

from .models import Comment
from django.utils.translation import gettext_lazy as _

# Другой вид формы для заполнения. Подходит для динамической формы
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# Форма для заполнения почты ( логично )
class EmailPostForm(forms.Form):
    name = forms.CharField(label = _('name'), max_length = 25)
    email = forms.EmailField(label = _('email'))
    to = forms.EmailField(label = _('to'))
    comments = forms.CharField(label = _('comment'), required = False, widget = forms.Textarea)

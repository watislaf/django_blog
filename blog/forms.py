from django import forms

from .models import Comment

# Другой вид формы для заполнения. Подходит для динамической формы
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# Форма для заполнения почты ( логично )
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length = 25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required = False,
                               widget = forms.Textarea)

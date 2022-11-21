from django import forms
from .models import Author, Comment, Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'tags')


class UserRegisterForm(forms.ModelForm):
    name = forms.TextInput()
    username = forms.TextInput()
    account_twitter = forms.TextInput()
    description = forms.Textarea()
    street = forms.TextInput()
    number = forms.TextInput()
    door = forms.TextInput()
    postal_code = forms.TextInput()
    city = forms.TextInput()
    number_phone = forms.TextInput()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = ['name', 'username', 'account_twitter', 'description', 'street',
                  'number', 'door', 'postal_code', 'city', 'number_phone', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class CommentForm(forms.ModelForm):
    content = forms.Textarea()

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'textAreaExample', 'rows': 4})
        }

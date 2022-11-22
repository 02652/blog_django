from django import forms
from .models import Author, Comment, Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'tags': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'Titulo de la noticia',
            'content': 'Contentido de la noticia',
            'tags': 'Ingrese las etiquetas de la noticia (ej: sociedad comida robo)'
        }


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
    password1 = forms.CharField(label="Ingrese su contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirme su contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        fields = ['name', 'username', 'account_twitter', 'description', 'street',
                  'number', 'door', 'postal_code', 'city', 'number_phone', 'password1', 'password2']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'account_twitter': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'door': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'number_phone': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'name': 'Ingrese su nombre',
            'username': 'Ingrese su nombre de usuario',
            'account_twitter': 'Ingrese su cuenta de twitter (ej: @usuario)',
            'description': 'Ingrese una breve descripcion de usted (ej: Soy una persona timida...)',
            'street': 'Ingrese la calle donde vive',
            'number': 'Numero de la calle',
            'door': 'Numero de su puerta',
            'postal_code': 'El codigo postal de su ciudad',
            'city': 'Ciudad',
            'number_phone': 'Numero o numeros de telefono (ej: 970566111, 877222221...)'
        }

        help_texts = {k: "" for k in fields}


class CommentForm(forms.ModelForm):
    content = forms.Textarea()

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'id': 'textAreaExample', 'rows': 4})
        }

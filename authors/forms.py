import re
from collections import defaultdict

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from mural.models import Mural


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'A senha deve ter pelo menos uma letra maiúscula, '
            'uma letra minúscula e um número. O comprimento deve ser '
            'pelo menos 8 caracteres.'
        ),
             code='invalid'
        )
    
 
class RegisterForm(forms.ModelForm):
    
    password = forms.CharField(
        required= True,
        widget=forms.PasswordInput(attrs= {
            'placeholder': 'Digite sua senha'
        }),
        validators=[strong_password]
    )

    confirmPassword = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs= {
            'placeholder': "Repita sua senha"
        }),
        error_messages= {
            'required': "Não pode ser vazia"
        }
    )

    class Meta:
        model= User
        fields= [ 'username', 'email', 'password']
        labels ={
            'username': "Digite seu usuário:"
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placegolder': "Digite o nome de usuário"
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': "Digite a sua senha"
            })
        }
        
    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')
        confirmPassword = cleaned_data.get('confirmPassword')
        if password != confirmPassword:
            raise ValidationError({
                'password':'As senhas não são iguais',
                'confirmPassword':'As senhas não são iguais'
            }
            )
        
class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    widget = { 
       'username': forms.TextInput(attrs={
           'placeholder': "Digite o nome de usuário"
       }),
       'password': forms.PasswordInput(attrs={
           'placeholder': "Digite sua senha"
       }
       )
    }

class AuthorPostForm(forms.ModelForm):

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categoria"].widget.attrs.update({"class": "span-2"})
        self.fields["oferece_ajuda"].widget.attrs.update({"class": "span-2"})

        self._my_errors = defaultdict(list)

    class Meta:
        model = Mural
        fields = 'title', 'description', 'contact', 'categoria', 'oferece_ajuda'
    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cd = self.cleaned_data

        title = cd.get('title')
        description = cd.get('description')


        if title == description:
            self._my_errors['title'].append('Não pode ser igual à descrição')
            self._my_errors['description'].append('Não pode ser igual ao título')
        
        if self._my_errors:
            raise ValidationError(self._my_errors)
        
        return super_clean
    
    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 5:
             self._my_errors['title'].append('Deve ter pelo menos 5 caracteres.')

        return title
    def clean_contact(self):
        field_name = 'contact'
        field_value = self.cleaned_data.get(field_name)

        if is_positive_number(field_value) < 0:
             self._my_errors[field_name].append('o número deve ser positivo')

        return field_value
    
def is_positive_number(value):
    try:
        number_string = float(value)
    except ValueError:
        return False
    return number_string > 0

        

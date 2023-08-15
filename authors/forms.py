from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



    
 
class RegisterForm(forms.ModelForm):

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
    

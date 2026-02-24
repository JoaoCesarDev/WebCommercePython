from django import forms
from django.contrib.auth import get_user_model


class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "Seu nome completo"
        },
        #    error_messages={'required': 'Obrigatório o preenchimento do nome'}

    )
    )
    email = forms.EmailField(widget=forms.EmailInput(
        # error_messages={'invalid': 'Digite um email válido!'},
        attrs={
            "class": "form-control",
            "placeholder": "Digite seu email"
        }
    )
    )
    content = forms.CharField(widget=forms.Textarea(
        #  error_messages={'required': 'É obrigatório o preenchimento do campo mensagem!'},
        attrs={
            "class": "form-control",
            "placeholder": "Digite sua mensagem"
        }
    )
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("O Email deve ser do gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


User = get_user_model()


def clean_username(self):
    username = self.cleaned_data.get('username')
    qs = User.objects.filter(username=username)
    if qs.exists():
        raise forms.ValidationError("Esse usuário já existe, escolha outro nome.")
    return username


def clean_email(self):
    email = self.cleaned_data.get('email')
    qs = User.objects.filter(email=email)
    if qs.exists():
        raise forms.ValidationError("Esse email já existe, digite outro email.")
    return email


def clean(self):
    data = self.cleaned_data
    password = self.cleaned_data.get('password')
    password2 = self.cleaned_data.get('password2')
    if password != password2:
        raise forms.ValidationError("As senhas informadas devem ser iguais!")
    return data

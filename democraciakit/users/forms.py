from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Pais
from django.contrib.auth.forms import PasswordChangeForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'ldap_password' in self.fields:
            del self.fields['ldap_password']

    frase = forms.CharField(
        max_length=256,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa un apodo, nombre o frase que te caracterice'}),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar email, este será tu nombre de usuari*'}),
    )
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingresar contraseña'}),
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repetir contraseña'}),
    )
    pais = forms.ModelChoiceField(
        queryset=Pais.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    municipio = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu Municipio'}),
    )
    cargo = forms.CharField(
        max_length=256,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu cargo'}),
    )
    foto = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'}),
    )
    descripcion = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingresa una descripción de tu trabajo'}),
    )

    class Meta:
        model = User
        fields = ['frase', 'email', 'password1', 'password2', 'pais', 'municipio', 'cargo', 'foto', 'descripcion']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email ya está registrado.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
    )


# Formulario para cambiar la contraseña del usuario
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña actual'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nueva contraseña'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repetir nueva contraseña'}))


# Formulario adicional para actualizar el perfil del usuario
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'pais')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control'}),
            'fotos': forms.FileInput(attrs={'class': 'form-control'}),
            'frase': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Este email ya está en uso por otro usuario.")
        return email
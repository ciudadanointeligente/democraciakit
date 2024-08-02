from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Pais

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    pais = forms.ModelChoiceField(
        queryset=Pais.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = User
        fields = ('email', 'pais', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email ya está registrado.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Set username to email for compatibility
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
    )

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise ValidationError("No existe una cuenta con este email.")
        return email

# Formulario adicional para actualizar el perfil del usuario
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'pais')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Este email ya está en uso por otro usuario.")
        return email
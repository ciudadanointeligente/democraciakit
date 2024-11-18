from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class Definicion1Form(forms.ModelForm):
    class Meta:
        model = Definicion1
        fields = ["uno", "dos", "tres", "cuatro"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
            "tres": forms.Textarea(attrs={"class": "form-control"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control"}),
        }


class Definicion1Edit(forms.ModelForm):
    class Meta:
        model = Definicion1
        fields = ["uno", "dos", "tres", "cuatro"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "dos": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "tres": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
        }


class Causas2Form(forms.ModelForm):
    class Meta:
        model = Causas2
        fields = ["uno", "dos", "tres", "cuatro"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
            "tres": forms.Textarea(attrs={"class": "form-control"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control"}),
        }


class Causas2Edit(forms.ModelForm):
    class Meta:
        model = Causas2
        fields = ["uno", "dos", "tres", "cuatro"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "dos": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "tres": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
        }


class Inclusivo2Form(forms.ModelForm):
    class Meta:
        model = Inclusivo2
        fields = ["uno", "dos", "tres", "cuatro", "cinco"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
            "tres": forms.Textarea(attrs={"class": "form-control"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control"}),
            "cinco": forms.Textarea(attrs={"class": "form-control"}),
        }


class Inclusivo2Edit(forms.ModelForm):
    class Meta:
        model = Inclusivo2
        fields = ["uno", "dos", "tres", "cuatro", "cinco"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "dos": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "tres": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
            "cinco": forms.Textarea(attrs={"class": "form-control", "rows": "3"}),
        }


class Mapadeafinidad2Form(forms.ModelForm):
    class Meta:
        model = Mapadeafinidad2
        fields = ["uno", "dos", "tres", "cuatro", "cinco"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
            "tres": forms.Textarea(attrs={"class": "form-control"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control"}),
            "cinco": forms.Textarea(attrs={"class": "form-control"}),
        }


class Mapadeactores4Form(forms.ModelForm):
    class Meta:
        model = Mapadeactores4
        fields = ["uno", "dos"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
            "tres": forms.Textarea(attrs={"class": "form-control"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control"}),
        }


class Oportunidades4Form(forms.ModelForm):
    class Meta:
        model = Oportunidades4
        fields = ["uno", "dos"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
        }


class Eventos4Form(forms.ModelForm):
    class Meta:
        model = Eventos4
        fields = ["uno", "dos"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
        }


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


# Formularios individuales para click to edit htmx en Mikit


class MikitDefinicion1Form(forms.ModelForm):
    class Meta:
        model = Definicion1
        fields = ["uno", "dos", "tres", "cuatro"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
            "tres": forms.Textarea(attrs={"class": "form-control"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control"}),
        }


class MikitCausas2Form(forms.ModelForm):
    class Meta:
        model = Causas2
        fields = ["uno", "dos", "tres", "cuatro"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
            "tres": forms.Textarea(attrs={"class": "form-control"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control"}),
        }


class MikitInclusivo2Form(forms.ModelForm):
    class Meta:
        model = Inclusivo2
        fields = ["uno", "dos", "tres", "cuatro", "cinco"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
            "tres": forms.Textarea(attrs={"class": "form-control"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control"}),
            "cinco": forms.Textarea(attrs={"class": "form-control"}),
        }


class MikitMapadeafinidad2Form(forms.ModelForm):
    class Meta:
        model = Mapadeafinidad2
        fields = ["uno", "dos", "tres", "cuatro", "cinco"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
            "tres": forms.Textarea(attrs={"class": "form-control"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control"}),
            "cinco": forms.Textarea(attrs={"class": "form-control"}),
        }


class MikitMapadeactores4Form(forms.ModelForm):
    class Meta:
        model = Mapadeactores4
        fields = ["uno", "dos"]
        widgets = {
            "uno": forms.Textarea(attrs={"class": "form-control"}),
            "dos": forms.Textarea(attrs={"class": "form-control"}),
            "tres": forms.Textarea(attrs={"class": "form-control"}),
            "cuatro": forms.Textarea(attrs={"class": "form-control"}),
        }

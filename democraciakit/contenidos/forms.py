from django import forms
from django.contrib.auth.models import User
from .models import *


class Definicion1Form(forms.ModelForm):
    class Meta:
        model = Definicion1
        fields = ['uno', 'dos', 'tres', 'cuatro']
        widgets = {
            'uno': forms.Textarea(attrs={'class': 'form-control'}),
            'dos': forms.Textarea(attrs={'class': 'form-control'}),
            'tres': forms.Textarea(attrs={'class': 'form-control'}),
            'cuatro': forms.Textarea(attrs={'class': 'form-control'}),
        }


class Causas2Form(forms.ModelForm):
    class Meta:
        model = Causas2
        fields = ['uno', 'dos', 'tres', 'cuatro']
        widgets = {
            'uno': forms.Textarea(attrs={'class': 'form-control'}),
            'dos': forms.Textarea(attrs={'class': 'form-control'}),
            'tres': forms.Textarea(attrs={'class': 'form-control'}),
            'cuatro': forms.Textarea(attrs={'class': 'form-control'}),
        }


class Inclusivo2Form(forms.ModelForm):
    class Meta:
        model = Inclusivo2
        fields = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
        widgets = {
            'uno': forms.Textarea(attrs={'class': 'form-control'}),
            'dos': forms.Textarea(attrs={'class': 'form-control'}),
            'tres': forms.Textarea(attrs={'class': 'form-control'}),
            'cuatro': forms.Textarea(attrs={'class': 'form-control'}),
            'cinco': forms.Textarea(attrs={'class': 'form-control'}),
        }


class Mapadeafinidad2Form(forms.ModelForm):
    class Meta:
        model = Mapadeafinidad2
        fields = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
        widgets = {
            'uno': forms.Textarea(attrs={'class': 'form-control'}),
            'dos': forms.Textarea(attrs={'class': 'form-control'}),
            'tres': forms.Textarea(attrs={'class': 'form-control'}),
            'cuatro': forms.Textarea(attrs={'class': 'form-control'}),
            'cinco': forms.Textarea(attrs={'class': 'form-control'}),
        }

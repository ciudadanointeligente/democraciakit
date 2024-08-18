from django.contrib.auth.models import AbstractUser
from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['nombre']

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, null=True, blank=True)
    municipio = models.CharField(max_length=100, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)
    cargo = models.CharField(max_length=256, null=True, blank=True)
    frase = models.CharField(max_length=256, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['email']


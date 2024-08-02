from django.db import models
from tinymce.models import HTMLField

class Categoria(models.Model):
    nombre = models.CharField(max_length=500, blank=True, null=True)
    subtitulo = models.CharField(max_length=500, blank=True, null=True)
    slug = models.CharField(max_length=500, blank=True, null=True)
    categoria = models.ForeignKey('self', related_name='categorias_hijas', on_delete=models.SET_NULL, null=True, blank=True)
    imagencategoria = models.ImageField(upload_to='imgs', blank=True, null=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Contenido(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = HTMLField()

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'
        ordering = ['titulo']

class Imagen(models.Model):
    titulo = models.CharField(max_length=500, blank=True, null=True)
    imagen = models.ImageField(upload_to='imgs', blank=True, null=True)
    contenido = models.ManyToManyField(Contenido, related_name='imagen', blank=True)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'

    def __str__(self):
        return self.titulo

class Archivos(models.Model):
    titulo = models.CharField(max_length=500, blank=True, null=True)
    archivo = models.FileField(upload_to='imgs', blank=True, null=True)
    contenido = models.ManyToManyField(Contenido, related_name='archivo', blank=True)
    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'

    def __str__(self):
        return self.titulo

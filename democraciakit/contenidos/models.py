from django.db import models
from users.models import CustomUser
from tinymce.models import HTMLField

class Etapa(models.Model):
    nombre = models.CharField(max_length=500, blank=True, null=True)
    slug = models.CharField(max_length=500, blank=True, null=True)
    subtitulo = models.CharField(max_length=500, blank=True, null=True)
    imagenetapa = models.ImageField(upload_to='imgs', blank=True, null=True)
    class Meta:
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    
    VALOR_CHOICES = (
        ('metodologias', 'Metodologías'),
        ('recomendaciones', 'Recomendaciones'),
        ('casosdeexito', 'Casos de éxito'),
    )

    nombre = models.CharField(max_length=500, blank=True, null=True)
    subtitulo = models.CharField(max_length=500, blank=True, null=True)
    slug = models.CharField(max_length=500, blank=True, null=True)
    etapa = models.ManyToManyField(Etapa, related_name='etapa', blank=True)
    imagencategoria = models.ImageField(upload_to='imgs', blank=True, null=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Contenido(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=500, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria', blank=True, null=True)
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
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='archivos', blank=True, null=True)
    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'

    def __str__(self):
        return self.titulo

class ArchivoMarcado(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='archivos_marcados')
    archivo = models.ForeignKey(Archivos, on_delete=models.CASCADE)
    fecha_marcado = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'archivo')

    def __str__(self):
        return f"{self.usuario.username} - {self.archivo.titulo}"

class Problemas(models.Model):
    problema = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='problemas_usuarios')
    fecha_problema = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'fecha_problema')

    def __str__(self):
        return f"{self.usuario.username} - {self.problema}"

# class ProblemasConceptos(models.Model):
#     problema = models.ForeignKey(Problemas, on_delete=models.CASCADE, related_name='problemas_conceptos')
#     contenido = models.TextField(blank=True, null=True)
#     class Meta:
#         verbose_name = 'Problema - Conceptos Iniciales'
#         verbose_name_plural = 'Problemas - Conceptos Iniciales'

#     def __str__(self):
#         return f"{self.problema.usuario.username} - {self.problema.fecha_problema}"

# class ProblemasDefinicion(models.Model):
#     problema = models.ForeignKey(Problemas, on_delete=models.CASCADE, related_name='problemas_definicion')
#     contenido = models.TextField(blank=True, null=True)
#     class Meta:
#         verbose_name = 'Problemas - Definición'
#         verbose_name_plural = 'Problemas - Definición'

#     def __str__(self):
#         return f"{self.problema.usuario.username} - {self.problema.fecha_problema}"

# class ProblemasEstrategia(models.Model):
#     problema = models.ForeignKey(Problemas, on_delete=models.CASCADE, related_name='problemas_estrategia')
#     contenido = models.TextField(blank=True, null=True)
#     class Meta:
#         verbose_name = 'Problemas - Estrategia'
#         verbose_name_plural = 'Problemas - Estrategia'

#     def __str__(self):
#         return f"{self.problema.usuario.username} - {self.problema.fecha_problema}"

# class ProblemasSesgo(models.Model):
#     problema = models.ForeignKey(Problemas, on_delete=models.CASCADE, related_name='problemas_sesgo')
#     contenido = models.TextField(blank=True, null=True)
#     class Meta:
#         verbose_name = 'Problemas - Sesgo'
#         verbose_name_plural = 'Problemas - Sesgo'

#     def __str__(self):
#         return f"{self.problema.usuario.username} - {self.problema.fecha_problema}"




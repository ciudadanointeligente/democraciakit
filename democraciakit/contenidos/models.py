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


class Definicion1(models.Model):
    uno = models.TextField(blank=True, null=True)
    dos = models.TextField(blank=True, null=True)
    tres = models.TextField(blank=True, null=True)
    cuatro = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='definicion1_usuarios')
    fecha_definicion1 = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'fecha_definicion1')
        verbose_name = 'Etapa #1 - Definición inicial'
        verbose_name_plural = 'Etapa #1 - Definiciones iniciales'
        ordering = ['-fecha_definicion1']

    def __str__(self):
        return f"{self.usuario.username} - definiciones iniciales - {self.fecha_definicion1}"


class Causas2(models.Model):
    uno = models.TextField(blank=True, null=True)
    dos = models.TextField(blank=True, null=True)
    tres = models.TextField(blank=True, null=True)
    cuatro = models.TextField(blank=True, null=True)
    cinco = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='causas2_usuarios')
    fecha_causas2 = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'fecha_causas2')
        verbose_name = 'Etapa #2 - Identificación de causas'
        verbose_name_plural = 'Etapa #2 - Identificación de causas'
        ordering = ['-fecha_causas2']

    def __str__(self):
        return f"{self.usuario.username} - identificación de causas - {self.fecha_causas2}"


class Inclusivo2(models.Model):
    uno = models.CharField(max_length=500, blank=True, null=True)
    dos = models.CharField(max_length=500, blank=True, null=True)
    tres = models.CharField(max_length=500, blank=True, null=True)
    cuatro = models.CharField(max_length=500, blank=True, null=True)
    cinco = models.CharField(max_length=500, blank=True, null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='inclusivo2_usuarios')
    fecha_inclusivo2 = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'fecha_inclusivo2')
        verbose_name = 'Etapa #2 - Enfoque inclusivo'
        verbose_name_plural = 'Etapa #2 - Enfoque inclusivo'
        ordering = ['-fecha_inclusivo2']

    def __str__(self):
        return f"{self.usuario.username} - enfoque inclusivo - {self.fecha_inclusivo2}"


class Mapadeafinidad2(models.Model):
    uno = models.TextField(blank=True, null=True)
    dos = models.TextField(blank=True, null=True)
    tres = models.TextField(blank=True, null=True)
    cuatro = models.TextField(blank=True, null=True)
    cinco = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='mapadeafinidad2_usuarios')
    fecha_mapadeafinidad2 = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'fecha_mapadeafinidad2')
        verbose_name = 'Etapa #2 - Mapa de afinidad'
        verbose_name_plural = 'Etapa #2 - Mapa de afinidad'
        ordering = ['-fecha_mapadeafinidad2']

    def __str__(self):
        return f"{self.usuario.username} - mapa de afinidad - {self.fecha_mapadeafinidad2}"


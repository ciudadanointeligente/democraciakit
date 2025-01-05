from django.db import models
from users.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class Definicion1(models.Model):
    uno = models.TextField("Quién", blank=True, null=True)
    dos = models.TextField("Dónde", blank=True, null=True)
    tres = models.TextField("Cuándo", blank=True, null=True)
    cuatro = models.TextField("Dolor", blank=True, null=True)
    usuario = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="definicion1_usuarios"
    )
    fecha_definicion1 = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("usuario", "fecha_definicion1")
        verbose_name = "Etapa #1 - Definición inicial"
        verbose_name_plural = "Etapa #1 - Definiciones iniciales"
        ordering = ["-fecha_definicion1"]
        get_latest_by = "fecha_definicion1"

    def __str__(self):
        return f"{self.usuario.username} - definiciones iniciales - {self.fecha_definicion1}"


class Causas2(models.Model):
    uno = models.TextField("Causa#1", blank=True, null=True)
    dos = models.TextField("Causa#2", blank=True, null=True)
    tres = models.TextField("Causa#3", blank=True, null=True)
    cuatro = models.TextField("Causa#4", blank=True, null=True)
    usuario = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="causas2_usuarios"
    )
    fecha_causas2 = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("usuario", "fecha_causas2")
        verbose_name = "Etapa #2 - Identificación de causas"
        verbose_name_plural = "Etapa #2 - Identificación de causas"
        ordering = ["-fecha_causas2"]
        get_latest_by = "fecha_causas2"

    def __str__(self):
        return (
            f"{self.usuario.username} - identificación de causas - {self.fecha_causas2}"
        )


class Inclusivo2(models.Model):
    uno = models.CharField("Reflexión #1", max_length=500, blank=True, null=True)
    dos = models.CharField("Reflexión #2", max_length=500, blank=True, null=True)
    tres = models.CharField("Reflexión #3", max_length=500, blank=True, null=True)
    cuatro = models.CharField("Reflexión #4", max_length=500, blank=True, null=True)
    cinco = models.CharField("Reflexión #5", max_length=500, blank=True, null=True)
    usuario = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="inclusivo2_usuarios"
    )
    fecha_inclusivo2 = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("usuario", "fecha_inclusivo2")
        verbose_name = "Etapa #2 - Enfoque inclusivo"
        verbose_name_plural = "Etapa #2 - Enfoque inclusivo"
        ordering = ["-fecha_inclusivo2"]
        get_latest_by = "fecha_inclusivo2"

    def __str__(self):
        return f"{self.usuario.username} - enfoque inclusivo - {self.fecha_inclusivo2}"


class Mapadeafinidad2(models.Model):
    uno = models.TextField("Quién", blank=True, null=True)
    dos = models.TextField("Dónde", blank=True, null=True)
    tres = models.TextField("Dolor", blank=True, null=True)
    cuatro = models.TextField("Cuándo", blank=True, null=True)
    cinco = models.TextField("Causa", blank=True, null=True)
    usuario = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="mapadeafinidad2_usuarios"
    )
    fecha_mapadeafinidad2 = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("usuario", "fecha_mapadeafinidad2")
        verbose_name = "Etapa #2 - Mapa de afinidad"
        verbose_name_plural = "Etapa #2 - Mapa de afinidad"
        ordering = ["-fecha_mapadeafinidad2"]
        get_latest_by = "fecha_mapadeafinidad2"

    def __str__(self):
        return (
            f"{self.usuario.username} - mapa de afinidad - {self.fecha_mapadeafinidad2}"
        )


class Mapadeactores4(models.Model):
    uno = models.TextField(blank=True, null=True)
    dos = models.TextField(blank=True, null=True)
    tres = models.TextField(blank=True, null=True)
    cuatro = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="mapadeactores4_usuarios"
    )
    fecha_mapadeactores2 = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("usuario", "fecha_mapadeactores2")
        verbose_name = "Etapa #4 - Mapa de actores"
        verbose_name_plural = "Etapa #4 - Mapa de actores"
        ordering = ["-fecha_mapadeactores2"]

    def __str__(self):
        return (
            f"{self.usuario.username} - mapa de actores - {self.fecha_mapadeactores2}"
        )


class Oportunidades4(models.Model):
    uno = models.TextField("Oportunidades", blank=True, null=True)
    dos = models.TextField("Amenazas", blank=True, null=True)
    usuario = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="oportunidades4_usuarios"
    )
    fecha_oportunidades4 = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("usuario", "fecha_oportunidades4")
        verbose_name = "Etapa #4 - Oportunidades"
        verbose_name_plural = "Etapa #4 - Oportunidades"
        ordering = ["-fecha_oportunidades4"]

    def __str__(self):
        return f"{self.usuario.username} - oportunidades - {self.fecha_oportunidades4}"


class Eventos4(models.Model):
    uno = models.TextField("Eventos", blank=True, null=True)
    dos = models.TextField("Acciones", blank=True, null=True)
    usuario = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="eventos4_usuarios"
    )
    fecha_eventos4 = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("usuario", "fecha_eventos4")
        verbose_name = "Etapa #4 - Eventos"
        verbose_name_plural = "Etapa #4 - Eventos"
        ordering = ["-fecha_eventos4"]

    def __str__(self):
        return f"{self.usuario.username} - eventos - {self.fecha_eventos4}"

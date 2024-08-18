from django.contrib import admin
from .models import Contenido, Imagen, Archivos, Categoria

admin.site.register(Contenido)
admin.site.register(Imagen)
admin.site.register(Archivos)
admin.site.register(Categoria)
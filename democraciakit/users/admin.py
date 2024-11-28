from django.contrib import admin
from .models import CustomUser, Pais


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "pais", "municipio")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Pais)

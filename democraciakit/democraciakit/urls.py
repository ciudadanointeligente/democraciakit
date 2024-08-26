from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_title = "DemocraciaKit"
admin.site.site_header = "DemocraciaKit"
admin.site.index_title = "DemocraciaKit panel"

urlpatterns = [
    path('paneldk/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('users/', include('users.urls')),
    path('', include('contenidos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.urls import path, include
from . import views

app_name = 'contenidos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mikit/', views.MikitView.as_view(), name='mikit'),
    path('rueda/', views.RuedaView.as_view(), name='rueda'),
    path('etapa1/', views.Etapa1View.as_view(), name='etapa1'),
    path('etapa1-conceptos/', views.Etapa1ConceptosView.as_view(), name='etapa1-conceptos'),
    path('etapa1-definicion/', views.Etapa1DefinicionView.as_view(), name='etapa1-definicion'),
]
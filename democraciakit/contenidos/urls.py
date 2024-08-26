from django.urls import path, include
from . import views

app_name = 'contenidos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mikit/', views.MikitView.as_view(), name='mikit'),
    path('rueda/', views.RuedaView.as_view(), name='rueda'),
    path('etapa1/', views.Etapa1View.as_view(), name='etapa1'),
    path('etapa1-conceptos/', views.Etapa1ConceptosView.as_view(), name='etapa1-conceptos'),
    path('etapa1-definicion/', views.Definicion1CreateView.as_view(), name='etapa1-definicion'),
    path('etapa1-estrategia/', views.Etapa1EstrategiaView.as_view(), name='etapa1-estrategia'),
    path('etapa1-sesgo/', views.Etapa1SesgoView.as_view(), name='etapa1-sesgo'),
    path('etapa2/', views.Etapa2View.as_view(), name='etapa2'),
    path('etapa2-matriz/', views.Etapa2MatrizView.as_view(), name='etapa2-matriz'),
    path('etapa2-mapaafinidad/', views.MapaAfinidad2CreateView.as_view(), name='etapa2-mapaafinidad'),
    path('etapa2-inclusivo/', views.Inclusivo2CreateView.as_view(), name='etapa2-inclusivo'),
    path('etapa2-identificacion/', views.IdentificacionCreateView.as_view(), name='etapa2-identificacion'),
    path('etapa3/', views.Etapa3View.as_view(), name='etapa3'),
    path('etapa4/', views.Etapa4View.as_view(), name='etapa4'),
    path('etapa5/', views.Etapa5View.as_view(), name='etapa5'),
    path('etapa6/', views.Etapa6View.as_view(), name='etapa6'),
    path('etapa7/', views.Etapa7View.as_view(), name='etapa7'),
]
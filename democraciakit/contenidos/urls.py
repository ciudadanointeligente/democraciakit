from django.urls import path, include
from . import views
from .views import *

app_name = 'contenidos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('mikit/', views.MikitView.as_view(), name='mikit'),
    path('derechos/', views.DerechosView.as_view(), name='derechos'),
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
    path('etapa3-3x3x3/', views.Etapa33x3x3View.as_view(), name='etapa3-3x3x3'),
    path('etapa3-sombreros/', views.Etapa3SombrerosView.as_view(), name='etapa3-sombreros'),
    path('etapa3-reflexionar/', views.Etapa3ReflexionarView.as_view(), name='etapa3-reflexionar'),
    path('etapa3-smart/', views.Etapa3SmartView.as_view(), name='etapa3-smart'),
    path('etapa4/', views.Etapa4View.as_view(), name='etapa4'),
    path('etapa4-proyeccion/', views.Etapa4ProyeccionView.as_view(), name='etapa4-proyeccion'),
    path('etapa4-mapaactores/', views.Etapa4MapaactoresView.as_view(), name='etapa4-mapaactores'),
    path('etapa4-eventos/', views.Etapa4EventosView.as_view(), name='etapa4-eventos'),
    path('etapa4-oportunidades/', views.Etapa4OportunidadesView.as_view(), name='etapa4-oportunidades'),
    path('etapa4-plandetrabajo/', views.Etapa4PlandetrabajoView.as_view(), name='etapa4-plandetrabajo'),
    path('etapa5/', views.Etapa5View.as_view(), name='etapa5'),
    path('etapa5-keepfixtry/', views.Etapa5KeepfixtryView.as_view(), name='etapa5-keepfixtry'),
    path('etapa5-impulsores/', views.Etapa5ImpulsoresView.as_view(), name='etapa5-impulsores'),
    path('etapa5-testeos/', views.Etapa5testView.as_view(), name='etapa5-testeos'),
    path('etapa6/', views.Etapa6View.as_view(), name='etapa6'),
    path('etapa6-metodos/', views.Etapa6MetodosView.as_view(), name='etapa6-metodos'),
    path('etapa6-casos/', views.Etapa6CasosView.as_view(), name='etapa6-casos'),
    path('etapa7/', views.Etapa7View.as_view(), name='etapa7'),
    path('etapa7-evaluacion/', views.Etapa7EvaluacionView.as_view(), name='etapa7-evaluacion'),
    path('etapa7-indicadores/', views.Etapa7IndicadoresView.as_view(), name='etapa7-indicadores'),
    path('etapa7-exito/', views.Etapa7ExitosView.as_view(), name='etapa7-exito'),
    path("films/", views.FilmList.as_view(), name='film-list')
]

htmx_urlpatterns = [
    path("add-film/", views.add_film, name="add-film"),
]

urlpatterns += htmx_urlpatterns
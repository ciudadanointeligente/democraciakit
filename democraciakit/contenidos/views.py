from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'contenidos/index.html'

class MikitView(TemplateView):
    template_name = 'contenidos/mikit.html'

class RuedaView(TemplateView):
    template_name = 'contenidos/rueda.html'

class Etapa1View(TemplateView):
    template_name = 'contenidos/etapa1.html'

class Etapa1ConceptosView(TemplateView):
    template_name = 'contenidos/etapa1-conceptos.html'

class Etapa1DefinicionView(TemplateView):
    template_name = 'contenidos/etapa1-definicion.html'
    
class Etapa2View(TemplateView):
    template_name = 'contenidos/etapa2.html'

class Etapa2MatrizView(TemplateView):
    template_name = 'contenidos/etapa2-matriz.html'

class Etapa2MapaAfinidadView(TemplateView):
    template_name = 'contenidos/etapa2-mapaafinidad.html'

class Etapa2InclusivoView(TemplateView):
    template_name = 'contenidos/etapa2-inclusivo.html'

class Etapa2IdentificacionView(TemplateView):
    template_name = 'contenidos/etapa2-identificacion.html'

class Etapa3View(TemplateView):
    template_name = 'contenidos/etapa3.html'

class Etapa4View(TemplateView):
    template_name = 'contenidos/etapa4.html'

class Etapa5View(TemplateView):
    template_name = 'contenidos/etapa5.html'

class Etapa6View(TemplateView):
    template_name = 'contenidos/etapa6.html'

class Etapa7View(TemplateView):
    template_name = 'contenidos/etapa7.html'

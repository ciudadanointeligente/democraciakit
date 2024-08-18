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
    

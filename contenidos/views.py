from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'contenidos/index.html'

class UnoView(TemplateView):
    template_name = 'contenidos/uno.html'

class DosView(TemplateView):
    template_name = 'contenidos/dos.html'

class TresView(TemplateView):
    template_name = 'contenidos/tres.html'

class CuatroView(TemplateView):
    template_name = 'contenidos/cuatro.html'

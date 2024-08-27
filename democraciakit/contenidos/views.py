from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from .models import *
from .forms import *
from django.http import HttpResponseRedirect


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


# class Definicion1CreateView(CreateView):
#     model = Definicion1
#     form_class = Definicion1Form
#     template_name = 'contenidos/etapa1-definicion.html'  

#     def form_valid(self, form):
#         form.instance.usuario = self.request.user  
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse('contenidos:etapa1-definicion')


class Definicion1CreateView(FormView):
    form_class = Definicion1Form
    template_name = 'contenidos/etapa1-definicion.html'
    success_url = reverse_lazy('contenidos:etapa1-definicion')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        # Guarda el formulario
        form.save()
        # Añade un mensaje de éxito
        messages.success(self.request, "¡Se han guardado tus definiciones!")
        return super().form_valid(form)  


class Etapa1EstrategiaView(TemplateView):
    template_name = 'contenidos/etapa1-estrategia.html'


class Etapa1SesgoView(TemplateView):
    template_name = 'contenidos/etapa1-sesgo.html'


class Etapa2View(TemplateView):
    template_name = 'contenidos/etapa2.html'


class IdentificacionCreateView(CreateView):
    model = Causas2
    form_class = Causas2Form
    template_name = 'contenidos/etapa2-identificacion.html'  # Reemplaza 'tu_app' con el nombre de tu aplicación

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asigna el usuario actual al objeto Causas2
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contenidos:etapa2-identificacion')  # Reemplaza con la URL de conexión deseada


class MapaAfinidad2CreateView(CreateView):
    template_name = 'contenidos/etapa2-mapaafinidad.html'
    model = Mapadeafinidad2
    form_class = Mapadeafinidad2Form

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contenidos:etapa2-mapaafinidad')


class Etapa2MatrizView(TemplateView):
    template_name = 'contenidos/etapa2-matriz.html'


class Inclusivo2CreateView(CreateView):
    template_name = 'contenidos/etapa2-inclusivo.html'
    model = Inclusivo2
    form_class = Inclusivo2Form

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contenidos:etapa2-inclusivo')
    


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

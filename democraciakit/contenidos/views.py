from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
User = get_user_model()


class IndexView(TemplateView):
    template_name = 'contenidos/index.html'


class MikitView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'contenidos/mikit.html'
    context_object_name = 'usuario'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['definicion1_usuarios'] = self.object.definicion1_usuarios.all().order_by('-fecha_definicion1')
        context['formulario_reciente1'] = self.object.definicion1_usuarios.order_by('-fecha_definicion1').first()
        context['causas2_usuarios'] = self.object.causas2_usuarios.all().order_by('-fecha_causas2')
        context['formulario_reciente2'] = self.object.causas2_usuarios.order_by('-fecha_causas2').first()
        context['inclusivo2_usuarios'] = self.object.inclusivo2_usuarios.all().order_by('-fecha_inclusivo2')
        context['formulario_reciente3'] = self.object.inclusivo2_usuarios.order_by('-fecha_inclusivo2').first()
        context['mapadeafinidad2_usuarios'] = self.object.mapadeafinidad2_usuarios.all().order_by('-fecha_mapadeafinidad2')
        context['formulario_reciente4'] = self.object.mapadeafinidad2_usuarios.order_by('-fecha_mapadeafinidad2').first()
        # context['mapadeactores4_usuarios'] = self.object.mapadeactores4_usuarios.all().order_by('-fecha_mapadeactores2')
        # context['formulario_reciente4'] = self.object.mapadeactores4_usuarios.order_by('-fecha_mapadeactores2').first()
        context['oportunidades4_usuarios'] = self.object.oportunidades4_usuarios.all().order_by('-fecha_oportunidades4')
        context['formulario_reciente41'] = self.object.oportunidades4_usuarios.order_by('-fecha_oportunidades4').first()
        context['eventos4_usuarios'] = self.object.eventos4_usuarios.all().order_by('-fecha_eventos4')
        context['formulario_reciente42'] = self.object.eventos4_usuarios.order_by('-fecha_eventos4').first()
        return context


class RuedaView(TemplateView):
    template_name = 'contenidos/rueda.html'


class Etapa1View(TemplateView):
    template_name = 'contenidos/etapa1.html'


class Etapa1ConceptosView(TemplateView):
    template_name = 'contenidos/etapa1-conceptos.html'


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


class IdentificacionCreateView(FormView):
    form_class = Causas2Form
    template_name = 'contenidos/etapa2-identificacion.html'
    success_url = reverse_lazy('contenidos:etapa2-identificacion')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        # Guarda el formulario
        form.save()
        # Añade un mensaje de éxito
        messages.success(self.request, "¡Se han guardado tus respuestas!")
        return super().form_valid(form)


class MapaAfinidad2CreateView(FormView):
    form_class = Mapadeafinidad2Form
    template_name = 'contenidos/etapa2-mapaafinidad.html'
    success_url = reverse_lazy('contenidos:etapa2-mapaafinidad')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        # Guarda el formulario
        form.save()
        # Añade un mensaje de éxito
        messages.success(self.request, "¡Se han guardado tus respuestas!")
        return super().form_valid(form)


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


class Etapa3SmartView(TemplateView):
    template_name = 'contenidos/etapa3-smart.html'


class Etapa3ReflexionarView(TemplateView):
    template_name = 'contenidos/etapa3-reflexionar.html'


class Etapa33x3x3View(TemplateView):
    template_name = 'contenidos/etapa3-3x3x3.html'


class Etapa3SombrerosView(TemplateView):
    template_name = 'contenidos/etapa3-sombreros.html'


class Etapa4View(TemplateView):
    template_name = 'contenidos/etapa4.html'


class Etapa4ProyeccionView(TemplateView):
    template_name = 'contenidos/etapa4-proyeccion.html'


class Etapa4MapaactoresView(FormView):
    form_class = Mapadeactores4Form
    template_name = 'contenidos/etapa4-mapaactores.html'
    success_url = reverse_lazy('contenidos:etapa4-mapaactores')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        # Guarda el formulario
        form.save()
        # Añade un mensaje de éxito
        messages.success(self.request, "¡Se han guardado tus respuestas!")
        return super().form_valid(form)


class Etapa4OportunidadesView(FormView):
    form_class = Oportunidades4Form
    template_name = 'contenidos/etapa4-oportunidades.html'
    success_url = reverse_lazy('contenidos:etapa4-oportunidades')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        # Guarda el formulario
        form.save()
        # Añade un mensaje de éxito
        messages.success(self.request, "¡Se han guardado tus respuestas!")
        return super().form_valid(form)


class Etapa4EventosView(FormView):
    form_class = Eventos4Form
    template_name = 'contenidos/etapa4-eventos.html'
    success_url = reverse_lazy('contenidos:etapa4-eventos')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        # Guarda el formulario
        form.save()
        # Añade un mensaje de válido
        messages.success(self.request, "¡Se han guardado tus respuestas!")
        return super().form_valid(form)


class Etapa4PlandetrabajoView(TemplateView):
    template_name = 'contenidos/etapa4-plandetrabajo.html'


class Etapa5View(TemplateView):
    template_name = 'contenidos/etapa5.html'


class Etapa5KeepfixtryView(TemplateView):
    template_name = 'contenidos/etapa5-keepfixtry.html'


class Etapa5ImpulsoresView(TemplateView):
    template_name = 'contenidos/etapa5-impulsores.html'


class Etapa5testView(TemplateView):
    template_name = 'contenidos/etapa5-testeos.html'


class Etapa6View(TemplateView):
    template_name = 'contenidos/etapa6.html'


class Etapa6MetodosView(TemplateView):
    template_name = 'contenidos/etapa6-metodos.html'


class Etapa6CasosView(TemplateView):
    template_name = 'contenidos/etapa6-casos.html'


class Etapa7View(TemplateView):
    template_name = 'contenidos/etapa7.html'


class Etapa7EvaluacionView(TemplateView):
    template_name = 'contenidos/etapa7-evaluacion.html'


class Etapa7IndicadoresView(TemplateView):
    template_name = 'contenidos/etapa7-indicadores.html'


class Etapa7ExitosView(TemplateView):
    template_name = 'contenidos/etapa7-exito.html'

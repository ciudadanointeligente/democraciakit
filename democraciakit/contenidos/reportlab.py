from django.views.generic import TemplateView
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth import get_user_model


User = get_user_model()


class IndexView(TemplateView):
    template_name = "contenidos/index.html"


class DerechosView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "contenidos/derechos.html"
    context_object_name = "usuario"

    def get_object(self):
        return self.request.user


class QueesView(TemplateView):
    template_name = "contenidos/partials/quees.html"


class MikitView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "contenidos/mikit.html"
    context_object_name = "usuario"

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["definicion1_usuarios"] = (
            self.object.definicion1_usuarios.all().order_by("-fecha_definicion1")
        )
        context["formulario_reciente1"] = self.object.definicion1_usuarios.order_by(
            "-fecha_definicion1"
        ).first()
        context["causas2_usuarios"] = self.object.causas2_usuarios.all().order_by(
            "-fecha_causas2"
        )
        context["formulario_reciente2"] = self.object.causas2_usuarios.order_by(
            "-fecha_causas2"
        ).first()
        context["inclusivo2_usuarios"] = self.object.inclusivo2_usuarios.all().order_by(
            "-fecha_inclusivo2"
        )
        context["formulario_reciente3"] = self.object.inclusivo2_usuarios.order_by(
            "-fecha_inclusivo2"
        ).first()
        context["mapadeafinidad2_usuarios"] = (
            self.object.mapadeafinidad2_usuarios.all().order_by("-fecha_mapadeafinidad2")
        )
        context["formulario_reciente4"] = self.object.mapadeafinidad2_usuarios.order_by(
            "-fecha_mapadeafinidad2"
        ).first()
        context["oportunidades4_usuarios"] = (
            self.object.oportunidades4_usuarios.all().order_by("-fecha_oportunidades4")
        )
        context["formulario_reciente41"] = self.object.oportunidades4_usuarios.order_by(
            "-fecha_oportunidades4"
        ).first()
        context["eventos4_usuarios"] = self.object.eventos4_usuarios.all().order_by(
            "-fecha_eventos4"
        )
        context["formulario_reciente42"] = self.object.eventos4_usuarios.order_by(
            "-fecha_eventos4"
        ).first()
        return context

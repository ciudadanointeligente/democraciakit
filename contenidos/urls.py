from django.urls import path, include
from . import views

app_name = 'contenidos'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('uno/', views.UnoView.as_view(), name='uno'),
    path('dos/', views.DosView.as_view(), name='dos'),
    path('tres/', views.TresView.as_view(), name='tres'),
    path('cuatro/', views.CuatroView.as_view(), name='cuatro'),
]
from django.urls import path
from . import views
from .forms import CustomAuthenticationForm

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password_reset/', views.password_reset, name='password_reset'),
]

htmx_urlpatterns = [
    path("check_username/", views.check_username, name="check_username"),
]

urlpatterns += htmx_urlpatterns
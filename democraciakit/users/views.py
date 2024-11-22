from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    CustomUserChangeForm,
)
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("contenidos:index")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("contenidos:index")
    else:
        form = CustomAuthenticationForm()
    return render(request, "users/user_login.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("users:profile")
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, "users/profile.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("contenidos:index")


def password_reset(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(
                request, user
            )  # Importante para mantener la sesión activa
            return redirect("contenidos:index")  # Redirige a una página de éxito
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, "users/password_reset.html", {"form": form})


def check_username(request):
    username = request.POST.get("username")
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse(
            "<div id='username-error' class='error'>This username is already taken</div>"
        )
    else:
        return HttpResponse(
            "<div id='username-error' class='success'>This username is available</div>"
        )


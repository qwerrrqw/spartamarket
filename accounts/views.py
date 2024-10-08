from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from users.models import Profile

from .forms import CustomUserCreationForm,CustomUserChangeForm
from users.models import Profile


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("products:product")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("products:product")


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            Profile.objects.create(user=user)
            return redirect("products:product")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("products:product")
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form":form}
    return render(request, "accounts/update.html", context)

def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect("products:product")

def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("products:product")
    else:    
        form = PasswordChangeForm(request.user)
    context = {"form": form}
    return render(request, "accounts/password_change.html", context)

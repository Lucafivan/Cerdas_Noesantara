from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from accounts.models import User

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/")  
        else:
            error = "Username atau password salah"
            return render(request, "theme/login.html", {"error": error})
    return render(request, "theme/login.html")

# theme/views.py
from django.shortcuts import render

def landing_view(request):
    return render(request, "theme/login.html")

from django.contrib.auth import get_user_model

User = get_user_model() 

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_of_birth = request.POST.get('date_of_birth')
        password = request.POST.get('password')

        # default untuk field yang ga ada di form
        is_staff = 0
        is_superuser = 0
        is_active = 1  # default aktif
        role = None
        last_login = None
        date_joined = None

        try:
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                date_of_birth=date_of_birth,
                password=make_password(password),
                is_staff=is_staff,
                is_superuser=is_superuser,
                is_active=is_active,
                role=role,
                last_login=last_login,
                date_joined=date_joined
            )
            messages.success(request, "Register berhasil! Silakan login.")
            return redirect('login')
        except IntegrityError:
            error = "Username atau email sudah terdaftar."
            return render(request, 'theme/register.html', {'error': error})
        except Exception as e:
            return render(request, 'theme/register.html', {'error': str(e)})

    return render(request, 'theme/register.html')
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_superuser:
                auth_login(request, user)
                return redirect("dashboard:index")
            else:
                return render(
                    request,
                    "users/login.html",
                    {"error_message": "Invalid credentials or not an admin."},
                )
        else:
            return render(
                request,
                "users/login.html",
                {"error_message": "Username and password are required."},
            )

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("users:login")

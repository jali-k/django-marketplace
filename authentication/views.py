from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        role = request.POST["role"]
        user = CustomUser.objects.create_user(
            username=username, password=password, role=role
        )
        login(request, user)
        return redirect("home")
    print("else")
    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")

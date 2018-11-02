from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.

# Login

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("posts")
        else:
            return render(request, "users/login.html", {"error": "Invalid Username or password"})
    return render(request, "users/login.html")

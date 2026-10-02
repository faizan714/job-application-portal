from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout


def signup(request):

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data["password"]
            )

            user.save()

            return redirect("login")

    else:
        form = SignupForm()

    return render(
        request,
        "accounts/signup.html",
        {"form": form}
    )


def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(
            request,
            "accounts/login.html",
            {"error": "Invalid username or password."}
        )

    return render(request, "accounts/login.html")



def user_logout(request):
    logout(request)
    return redirect("login")


from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(
        request,
        "accounts/dashboard.html"
    )


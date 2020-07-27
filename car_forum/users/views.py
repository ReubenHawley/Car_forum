from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("Username")
            messages.success(request, f"thank you {username}, you're all signed up!")
            return redirect("login")
    else:
        form = UserRegisterFrom()
    return render(request, 'users/register.html', {"form": form})


@login_required
def mycar(request):
    context = {
        "mydata": "dummy data"
    }
    return render(request, "users/mycar.html", context)

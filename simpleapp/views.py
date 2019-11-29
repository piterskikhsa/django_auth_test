from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from simpleapp.forms import SingUpForm


def sign_up(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('simple_app:index')
    else:
        form = SingUpForm()
    return render(request, 'registration/signup-page.html', {'form': form})


@login_required(login_url='simple_app:sign_up')
def index(request):
    return render(request, 'home-page.html')


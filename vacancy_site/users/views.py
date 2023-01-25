from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('qa-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



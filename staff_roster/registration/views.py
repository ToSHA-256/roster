from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .form import RegisterUserForm
from django.contrib.auth import authenticate, login
@csrf_protect
def register_view(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            redirect_url = 'index'
            return redirect(redirect_url)
        # Если форма неверна, поля не будут опустошаться
        print("Form errors:", form.errors)
        error_message = 'Некорректные данные при регистрации'
        return render(request, 'registration/registration.html', {'form': form, 'error_message': error_message})
    else:
        form = RegisterUserForm()
        return render(request, 'registration/registration.html', {'form': form})

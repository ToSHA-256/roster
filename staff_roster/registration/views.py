from django.shortcuts import render, redirect

from .form import CustomUserCreationForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

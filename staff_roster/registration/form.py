from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='Имя:', widget=forms.TextInput(attrs={'class': 'blank-input'}))
    patronymic = forms.CharField(label='Отчество:', widget=forms.TextInput(attrs={'class': 'blank-input'}))
    last_name = forms.CharField(label='Фамилия:', widget=forms.TextInput(attrs={'class': 'blank-input'}))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'blank-input'}))
    password2 = forms.CharField(label='Подтверждение пароля:',
                                widget=forms.PasswordInput(attrs={'class': 'blank-input'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'patronymic', 'password1', 'password2')

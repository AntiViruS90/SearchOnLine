from django import forms as f

""" Нам нужна специальная форма для регистрации пользователя,
которая есть в библиотеке Django, смотреть ниже"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    username = f.CharField(label='Login', help_text='')
    password1 = f.CharField(label='Password', help_text='',
                            widget=f.PasswordInput())
    # # PasswordInput() позволяет вводить пароль точками
    password2 = f.CharField(label='Confirm password', help_text='',
                            widget=f.PasswordInput(attrs={'autocomplete': 'new-password'}))
    first_name = f.CharField(label='First Name', required=True, max_length=20)
    last_name = f.CharField(label='Last Name', max_length=30)
    email = f.EmailField(label='Email',
                         widget=f.TextInput(attrs={'placeholder': 'example@example.com'}))

    # class Meta:  # при помощи Meta мы получаем поля из БД Models
    #     model = User
    #     fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

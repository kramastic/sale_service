from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Objects


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput())
    email = forms.EmailField(label="E-mail", widget=forms.TextInput())
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="Повторите пароль", widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={"placeholder": "enter your login"}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "enter your password"}
        ),
    )


class AdvForm(forms.ModelForm):
    class Meta:
        model = Objects
        fields = (
            "category",
            "title",
            "address",
            "description",
            "price",
            "image_id",
        )

    category = forms.ChoiceField(
        choices=(
            ("__empty__", "Выбрать"),
            ("Квартира", "Квартира"),
            ("Дом", "Дом"),
            ("Гараж", "Гараж"),
        ),
        label="Категория",
    )
    price = forms.IntegerField(label="Цена (руб.)")

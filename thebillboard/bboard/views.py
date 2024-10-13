from typing import Any

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from bboard.forms import AdvForm, LoginUserForm, RegisterUserForm
from bboard.models import Objects


class GetAllAdvView(ListView):
    template_name = "bboard/main_page.html"
    ordering = ["-time create"]

    def get_queryset(self) -> QuerySet[Any]:
        return Objects.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.get_queryset()
        context["title"] = "Доска объявлений"
        context["categories"] = ["Квартиры", "Дома", "Гаражи"]
        return context


class GetAdvByCategory(ListView):
    template_name = "bboard/by_category.html"
    ordering = ["-time create"]

    def get_queryset(self) -> QuerySet[Any]:
        categories = {
            "Квартиры": "Квартира",
            "Гаражи": "Гараж",
            "Дома": "Дом",
        }
        return Objects.objects.filter(
            category=categories[f'{self.kwargs["cat"]}']
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.get_queryset()
        context["title"] = f'{self.kwargs["cat"]}'
        context["categories"] = ["Квартиры", "Дома", "Гаражи"]
        return context


class ShowAdv(DetailView):
    model = Objects
    template_name = "bboard/show_adv.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_object()
        context["categories"] = ["Квартиры", "Дома", "Гаражи"]
        context["title"] = self.get_object().title
        return context


class AddAdv(CreateView):
    template_name = "bboard/create_bb.html"
    form_class = AdvForm
    # model = Objects
    # fields = "__all__"
    # success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["categories"] = ["Квартиры", "Дома", "Гаражи"]
        context["title"] = "Разместить объявление"
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "bboard/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Войти"
        return context

    def get_success_url(self):
        return reverse_lazy("main")


class Logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy("main")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "bboard/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("main")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Зарегистрироваться"
        return context


class MyAdv(ListView):
    template_name = "bboard/my_adv.html"
    ordering = ["-time create"]

    def get_queryset(self) -> QuerySet[Any]:
        return Objects.objects.filter(user_id=self.kwargs["pk"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.get_queryset()
        context["title"] = "Мои объявления"
        context["categories"] = ["Квартиры", "Дома", "Гаражи"]
        return context


class EditAdv(UpdateView):
    form_class = AdvForm
    template_name = "bboard/edit_adv.html"

    def get_object(self):
        return Objects.objects.get(id=self.kwargs["pk"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ["Квартиры", "Дома", "Гаражи"]
        context["title"] = "Редактировать объявления"
        context["object"] = self.get_object()
        return context


class DeleteAdv(DeleteView):
    model = Objects
    template_name = "bboard/confirm_delete.html"

    def get_success_url(self):
        user_id = self.get_object().user_id
        return reverse_lazy("my_adv", args=[user_id])

    def get_object(self):
        print(self.kwargs)
        return Objects.objects.get(id=self.kwargs["pk"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = ["Квартиры", "Дома", "Гаражи"]
        context["object"] = self.get_object()
        return context

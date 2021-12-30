from django.contrib.auth.forms import UserModel, UsernameField
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login

from .forms import RegisterUserForm, LoginUserForm


names_igor = ['Игорь', 'Igor']
names_alya = ['Аля', 'Алевтина', 'Alya', 'Alevtina']
names_arti = ['Артем', 'Артём', 'Arti', 'Artyom']
names_roma = ['Рома', 'Roma', 'Roman', 'Роман']
names_anton = ['Антон', 'Тоха', 'Антоха', 'Tony', 'Anton', 'Antony']

def homepage(request):
    return render(request, 'newyear/homepage.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'newyear/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        if self.request.user.username.capitalize() in names_igor:
            return redirect('igor')
        elif self.request.user.username.capitalize() in names_alya:
            return redirect('alya')
        elif self.request.user.username.capitalize() in names_roma:
            return redirect('roma')
        elif self.request.user.username.capitalize() in names_arti:
            return redirect('arti')
        elif self.request.user.username.capitalize() in names_anton:
            return redirect('anton')
        else:
            return redirect('homepage')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'newyear/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('homepage')

    def get_success_url(self):
    
        if self.request.user.username.capitalize() in names_igor:
            return reverse_lazy('igor')
        elif self.request.user.username.capitalize() in names_alya:
            return reverse_lazy('alya')
        elif self.request.user.username.capitalize() in names_roma:
            return reverse_lazy('roma')
        elif self.request.user.username.capitalize() in names_arti:
            return reverse_lazy('arti')
        elif self.request.user.username.capitalize() in names_anton:
            return reverse_lazy('anton')
        else:
            return reverse_lazy('homepage')


def logout_user(request):
    logout(request)
    return redirect('login')

def igor(request):
    return render(request, 'newyear/igor.html')

def alya(request):
    return render(request, 'newyear/alya.html')

def roma(request):
    return render(request, 'newyear/roma.html')

def arti(request):
    return render(request, 'newyear/arti.html')

def anton(request):
    return render(request, 'newyear/anton.html')

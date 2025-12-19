from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Films
from .forms import FilmsForm


# FILMS

class AllFilmsListView(LoginRequiredMixin, generic.ListView):
    model = Films
    template_name = 'cineboard/list_page.html'
    context_object_name = 'films'


class CreateFilmView(LoginRequiredMixin, generic.CreateView):
    model = Films
    form_class = FilmsForm
    template_name = 'cineboard/form_page.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить фильм'
        return context


class UpdateFilmView(LoginRequiredMixin, generic.UpdateView):
    model = Films
    form_class = FilmsForm
    template_name = 'cineboard/form_page.html'
    success_url = '/'

    def get_object(self):
        return get_object_or_404(Films, id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать фильм'
        return context


def delete_film(request, id):
    film = get_object_or_404(Films, id=id)
    if request.method == 'POST':
        film.delete()
        return redirect('/')
    return render(request, 'cineboard/form_page.html', {
        'title': 'Удалить фильм',
        'form': None
    })


# AUTH

class RegisterView(generic.View):
    def get(self, request):
        return render(request, 'cineboard/form_page.html', {
            'form': UserCreationForm(),
            'title': 'Регистрация'
        })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'cineboard/form_page.html', {
            'form': form,
            'title': 'Регистрация'
        })


class LoginView(generic.View):
    def get(self, request):
        return render(request, 'cineboard/form_page.html', {
            'form': AuthenticationForm(),
            'title': 'Вход'
        })

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
        return render(request, 'cineboard/form_page.html', {
            'form': form,
            'title': 'Вход'
        })


def logout_view(request):
    logout(request)
    return redirect('/login/')

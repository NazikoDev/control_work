from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models, forms
from django.http import HttpResponse




class CreateFilmView(generic.CreateView):
    model = models.Films
    form_class = forms.FilmsForm
    template_name = 'cineboard/pages/movie_add_page.html'
    success_url = '/all_films/'


class UpdateFilmView(generic.UpdateView):
    model = models.Films
    form_class = forms.FilmsForm
    template_name = 'cineboard/pages/movie_edit_page.html'
    success_url = '/all_films/'

    def get_object(self, *args, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.Films, id=film_id)


class DeleteFilmView(generic.DeleteView):
    template_name = 'cineboard/pages/movie_remove_page.html'
    success_url = '/all_films/'

    def get_object(self, *args, **kwargs):
        film_id = self.kwargs.get('id')
        return get_object_or_404(models.Films, id=film_id)


class AllFilmsListView(LoginRequiredMixin, generic.ListView):
    model = models.Films
    template_name = 'cineboard/pages/movies_overview.html'
    context_object_name = 'tv_lst'


# ================== AUTH ==================

class RegisterView(generic.View):
    def get(self, request):
        form = UserCreationForm()
        return render(
            request,
            'cineboard/users/signup_page.html',
            {'form': form}
        )

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cineboard:login')
        return render(
            request,
            'cineboard/users/signup_page.html',
            {'form': form}
        )


class AuthLoginView(generic.View):
    def get(self, request):
        form = AuthenticationForm()
        return render(
            request,
            'cineboard/users/signin_page.html',
            {'form': form}
        )

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('cineboard:all_films')
        return render(
            request,
            'cineboard/users/signin_page.html',
            {'form': form }
        )


class AuthLogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('cineboard:login')

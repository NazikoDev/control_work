from django.urls import path
from . import views

app_name = 'cineboard'

urlpatterns = [
    # AUTH
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

    # FILMS
    path('', views.AllFilmsListView.as_view(), name='all_films'),
    path('film/create/', views.CreateFilmView.as_view(), name='create_film'),
    path('film/<int:id>/edit/', views.UpdateFilmView.as_view(), name='update_film'),
    path('film/<int:id>/delete/', views.delete_film, name='delete_film'),
]

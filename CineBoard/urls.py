from django.urls import path
from .import views

app_name='cineboard'

urlpatterns = [
    path('register_cine/', views.RegisterView.as_view(), name='register_cine'),
    path('login_cine/', views.AuthLoginView.as_view(), name='login_cine'),
    path('logout_cine/', views.AuthLogoutView.as_view(), name='logout_cine'),
    path('all_films/', views.AllFilmsListView.as_view(), name='all_films'),
    path('all_films/<int:id>/update/', views.UpdateFilmView.as_view(), name='update'),
    path('all_films/<int:id>/delete/', views.DeleteFilmView.as_view(), name='delete'),
    path('create_film/', views.CreateFilmView.as_view(), name='create_film')
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_list, name='movies_list'),
    path('about_us', views.about_us, name='about_us'),
    path('movie_detail/<int:pk>/',views.movie_detail, name='movie_detail')
]


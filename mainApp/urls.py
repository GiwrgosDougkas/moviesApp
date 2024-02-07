from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about_us', views.about_us, name='about_us'),
]


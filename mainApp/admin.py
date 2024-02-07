from django.contrib import admin

from mainApp.models import Movie, Category, Studio, Director

# Register your models here.
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Studio)
admin.site.register(Director)

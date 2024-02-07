from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.category


class Studio(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Director(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    genre = models.CharField(max_length=10, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    genre = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    cv = models.FileField(upload_to='cv_files')

    def __str__(self):
        return self.last_name + " " + self.first_name


class Movie(models.Model):
    title = models.CharField(max_length=250)
    duration_minutes = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.DateField()
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    stream_url = models.CharField(max_length=250)
    summary = models.TextField()
    image = models.ImageField(upload_to='movies_images', null=True);


    def __str__(self):
        return self.title

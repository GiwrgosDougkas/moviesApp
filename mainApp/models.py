from django.db import models


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    rating = models.FloatField()
    stuido = models.CharField(max_length=250)

    def __str__(self):
        return self.title

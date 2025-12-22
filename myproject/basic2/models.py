from django.db import models

# Create your models here.

class moviereview(models.Model):
    movie_name=models.CharField(max_length=100)
    release_date=models.CharField(max_length=100)
    budget=models.CharField(max_length=100)
    rating=models.IntegerField()
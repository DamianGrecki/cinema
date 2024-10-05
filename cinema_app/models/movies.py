# models.py
from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()

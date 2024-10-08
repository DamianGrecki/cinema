# models.py
from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=False)
    release_at = models.DateTimeField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media/', default='missing_movie_image.jpg')

    def __str__(self):
        return self.title

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=63, unique=True)

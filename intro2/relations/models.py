from django.db import models

# Create your models here.

# One to many
class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"


class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

# OneToOneField

# Many to many
class Movie(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.title}"


class Character(models.Model):
    name = models.CharField(max_length=10)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return f"{self.name}"

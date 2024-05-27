from django.db import models

# Create your models here.
class MovieDb(models.Model):
    Movie_Title     =   models.CharField(max_length=30)
    ReleasedYear    =   models.IntegerField(null=True)
    Description     =   models.TextField()
    def __str__(self):
        return self.Movie_Title
class Director(models.Model):
    DirectorName    =   models.CharField(max_length=40)
    def __str__(self):
        return self.DirectorName
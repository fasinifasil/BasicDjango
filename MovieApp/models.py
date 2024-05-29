from django.db import models

# Create your models here.


class CensorInfo(models.Model):
    rating      =   models.CharField(max_length=20,null=True)
    certifedBy  =   models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.certifedBy

class MovieDb(models.Model):
    Movie_Title     =   models.CharField(max_length=30)
    ReleasedYear    =   models.IntegerField(null=True)
    Description     =   models.TextField()
    MoviePic        =   models.ImageField(upload_to='poster',null=True)
    censoredBy      =   models.OneToOneField(CensorInfo,on_delete=models.CASCADE,related_name='movie',null=True)
    def __str__(self):
        return self.Movie_Title
class Director(models.Model):
    DirectorName    =   models.CharField(max_length=40)
    def __str__(self):
        return self.DirectorName



from django.db import models

class movie(models.Model):
    title = models.CharField('Title', max_length=100)
    director = models.CharField('Director', max_length=50)
    release = models.DateField('Release')
    genre = models.CharField('Genre', max_length=30)
    

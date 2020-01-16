from django.db import models

# Create your models here.

class Meme(models.Model):
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
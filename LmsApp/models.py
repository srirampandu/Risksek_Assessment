from django.db import models

# Create your models here.


class Library(models.Model):
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    ISBN = models.IntegerField()


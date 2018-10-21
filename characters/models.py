from django.db import models

# Create your models here.

class Character(models.Model):
    external_id = models.IntegerField()
    name = models.CharField(max_length=120)
    description = models.TextField()
    modified = models.DateField()
    resourceURI = models.CharField(max_length=255)
    thumbail = models.CharField(max_length=255)
    comics = models.ForeignKey('Comics', on_delete=models.CASCADE)

class Comics(models.Model):
    name = models.CharField(max_length=180)

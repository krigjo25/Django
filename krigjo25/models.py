
from django.db import models

# Create your models here.
class MyProjects(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    tech = models.CharField(max_length=20)
    img = models.FilePathField(path='/img')

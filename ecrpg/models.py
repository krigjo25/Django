from django.db import models

# Create your models here.

class AdminTeam(models.Model):

    userName = models.CharField(max_length=60)
    lvl = models.IntegerField()
    boss = models.CharField(max_length=60)
    img = models.FilePathField(path = '/img')

class ecrpgWiki(models.CharField):
    pass
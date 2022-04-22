from django.db import models

# Create your models here.

class AdminTeam(models.Model):

    userName = models.CharField(max_length=60)
    lvl = models.IntegerField()
    boss = models.CharField(max_length=60)
    img = models.FilePathField(path = '/img')

class WikiCategory(models.Model):

    category = models.CharField(max_length=20)

class WikiPost(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    categories = models.ManyToManyField('Category', related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

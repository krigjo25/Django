from django.db import models

# Create your models here.


class ManagementTeamlvl3(models.Model):

    memberName = models.CharField(max_length=60)
    lvl = models.IntegerField(default=3)
    boss = models.CharField(max_length=60)
    img = models.FilePathField(path = '/img')

class ManagementTeamlvl2(models.Model):

    memberName = models.CharField(max_length=60)
    lvl = models.IntegerField(default=2)
    boss = models.CharField(max_length=60)
    img = models.FilePathField(path = '/img')

class ManagementTeam(models.Model):

    memberName = models.CharField(max_length=60)
    lvl = models.IntegerField(default=1)
    boss = models.CharField(max_length=60)
    img = models.FilePathField(path = '/img')

class ManagementTeamHelper(models.Model):

    memberName = models.CharField(max_length=60)
    boss = models.CharField(max_length=60)
    img = models.FilePathField(path = '/img')

class WikiCategory(models.Model):

    category = models.CharField(max_length=20)

class WikiPost(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    categories = models.ManyToManyField('WikiCategory', related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

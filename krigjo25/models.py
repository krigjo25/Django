
from django.db import models

#   Portefolio Table

class DatabaseProjects(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.FilePathField(path='/img', default='/img/logo/sql.svg')
    link = models.TextField(default='https://github.com/krigjo25?tab=repositories')

class PythonProjects(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    tech = models.CharField(max_length=20)
    img = models.FilePathField(path='/img', default='demo.jpg')
    link = models.TextField(default='https://github.com/krigjo25?tab=repositories')

class DiscordBots(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.FilePathField(path='/img', default='/img/logo/python.svg')
    link = models.TextField(default='https://github.com/krigjo25?tab=repositories')

#   The Blog
class BlogCategory(models.Model):

    category = models.CharField(max_length=20)

class Post(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    categories = models.ManyToManyField('BlogCategory', related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):

    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add= True)

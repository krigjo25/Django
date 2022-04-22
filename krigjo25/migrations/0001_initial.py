# Generated by Django 4.0.4 on 2022-04-22 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DatabaseProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img', models.FilePathField(default='/img/logo/sql.svg', path='/img')),
                ('link', models.TextField(default='https://github.com/krigjo25?tab=repositories')),
            ],
        ),
        migrations.CreateModel(
            name='DiscordBots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img', models.FilePathField(default='/img/logo/python.svg', path='/img')),
                ('link', models.TextField(default='https://github.com/krigjo25?tab=repositories')),
            ],
        ),
        migrations.CreateModel(
            name='PythonProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('tech', models.CharField(max_length=20)),
                ('img', models.FilePathField(default='demo.jpg', path='/img')),
                ('link', models.TextField(default='https://github.com/krigjo25?tab=repositories')),
            ],
        ),
        migrations.CreateModel(
            name='Responsories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img', models.FilePathField(default='/img/logo/python.svg', path='/img')),
                ('link', models.TextField(default='https://github.com/krigjo25?tab=repositories')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('categories', models.ManyToManyField(related_name='posts', to='krigjo25.blogcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='krigjo25.post')),
            ],
        ),
    ]

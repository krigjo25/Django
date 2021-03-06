# Generated by Django 4.0.4 on 2022-05-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannedPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerName', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('reason', models.CharField(max_length=255)),
                ('adminName', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ManagementTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerName', models.CharField(max_length=255)),
                ('lvl', models.IntegerField()),
                ('boss', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WikiCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img', models.FilePathField(blank=True, path='/svg')),
            ],
        ),
        migrations.CreateModel(
            name='WikiPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(related_name='posts', to='ecrpg.wikicategory')),
            ],
        ),
    ]

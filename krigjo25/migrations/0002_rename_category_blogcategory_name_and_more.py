# Generated by Django 4.0.4 on 2022-04-27 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krigjo25', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcategory',
            old_name='category',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='categories',
            new_name='category',
        ),
    ]

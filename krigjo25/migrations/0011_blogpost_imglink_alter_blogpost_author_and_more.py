# Generated by Django 4.0.4 on 2022-05-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krigjo25', '0010_rename_bot_blogpost_botlink_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='imglink',
            field=models.FilePathField(default='img/svg/', path='/img'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='krigjo25', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='botlink',
            field=models.CharField(default='https://discord.com/api/oauth2/authorize?client_id=903619759587852338&permissions=8&scope=bot', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='readmelink',
            field=models.CharField(default='https://github.com/krigjo25/Discord', max_length=255),
        ),
    ]

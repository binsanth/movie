# Generated by Django 4.2.5 on 2023-10-01 04:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_rename_movie_movie_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_table',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='pics'),
            preserve_default=False,
        ),
    ]

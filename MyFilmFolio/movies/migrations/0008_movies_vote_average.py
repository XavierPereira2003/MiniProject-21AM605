# Generated by Django 5.0.3 on 2024-05-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_rename_director_id_movies_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='vote_average',
            field=models.FloatField(default=0.0),
        ),
    ]

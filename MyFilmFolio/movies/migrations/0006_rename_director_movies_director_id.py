# Generated by Django 5.0.3 on 2024-05-03 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_rename_discription_movies_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='director',
            new_name='director_id',
        ),
    ]

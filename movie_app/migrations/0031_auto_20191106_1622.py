# Generated by Django 2.2.6 on 2019-11-06 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0030_movie_total_ratings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='total_ratings',
            new_name='times_rated',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='rating',
            new_name='total_rating',
        ),
    ]

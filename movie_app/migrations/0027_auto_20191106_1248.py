# Generated by Django 2.2.6 on 2019-11-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0026_auto_20191105_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cast',
            field=models.ManyToManyField(blank=True, related_name='movies', to='movie_app.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='movies', to='movie_app.Genre'),
        ),
    ]

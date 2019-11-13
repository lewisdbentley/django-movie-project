# Generated by Django 2.2.6 on 2019-11-04 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0015_auto_20191104_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie_app.Movie'),
        ),
    ]

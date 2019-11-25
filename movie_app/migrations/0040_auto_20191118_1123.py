# Generated by Django 2.2.6 on 2019-11-18 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0039_auto_20191111_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='director',
            name='comments',
        ),
        migrations.AddField(
            model_name='movie',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movie_app.Profile'),
        ),
    ]

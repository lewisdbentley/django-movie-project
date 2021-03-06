# Generated by Django 2.2.6 on 2019-11-06 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0033_auto_20191106_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='directed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='movie_app.Director'),
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0021_auto_20191105_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-22 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoGuessr', '0008_game_score_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_score',
            name='username',
            field=models.CharField(default='null'),
        ),
    ]

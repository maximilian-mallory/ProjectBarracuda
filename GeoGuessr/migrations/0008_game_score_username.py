# Generated by Django 5.0.3 on 2024-04-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoGuessr', '0007_remove_game_score_playerid_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_score',
            name='username',
            field=models.CharField(default=''),
        ),
    ]

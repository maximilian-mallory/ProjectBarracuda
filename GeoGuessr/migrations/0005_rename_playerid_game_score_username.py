# Generated by Django 5.0.3 on 2024-04-22 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GeoGuessr', '0004_alter_game_score_playerid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game_score',
            old_name='playerID',
            new_name='username',
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game_Score',
            fields=[
                ('gameID', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('finalTime', models.IntegerField()),
                ('usedHintOne', models.BooleanField(default=False)),
                ('usedHintTwo', models.BooleanField(default=False)),
                ('datePlayed', models.DateTimeField()),
                ('playerID', models.IntegerField()),
            ],
        ),
    ]
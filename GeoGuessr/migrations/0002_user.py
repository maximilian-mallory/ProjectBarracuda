# Generated by Django 5.0.3 on 2024-04-07 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoGuessr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('playerID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

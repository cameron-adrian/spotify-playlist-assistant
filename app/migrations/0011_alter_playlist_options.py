# Generated by Django 4.2 on 2024-07-22 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_playlist_average_song_length'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playlist',
            options={'ordering': ['name']},
        ),
    ]

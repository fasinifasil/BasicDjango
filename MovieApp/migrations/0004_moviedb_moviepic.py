# Generated by Django 5.0.6 on 2024-05-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0003_director_alter_moviedb_releasedyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedb',
            name='MoviePic',
            field=models.ImageField(null=True, upload_to='poster'),
        ),
    ]

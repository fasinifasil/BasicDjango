# Generated by Django 5.0.6 on 2024-05-29 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0007_rename_censoredby_moviedb_certifedby'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviedb',
            old_name='certifedBy',
            new_name='censoredBy',
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0004_moviedb_moviepic'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=20, null=True)),
                ('certifedBy', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
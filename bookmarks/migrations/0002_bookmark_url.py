# Generated by Django 2.0.6 on 2018-06-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='url',
            field=models.URLField(default='Your Website'),
        ),
    ]

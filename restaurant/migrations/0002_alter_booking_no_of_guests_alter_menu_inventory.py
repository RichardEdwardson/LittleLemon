# Generated by Django 4.2.9 on 2024-01-09 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.SmallIntegerField(),
        ),
    ]

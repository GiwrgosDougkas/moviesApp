# Generated by Django 4.2.9 on 2024-02-07 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='genre',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
    ]

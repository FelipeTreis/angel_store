# Generated by Django 4.0.5 on 2022-07-29 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
        ('angel', '0007_alter_clothes_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='brands',
            field=models.ManyToManyField(to='brand.brand'),
        ),
    ]

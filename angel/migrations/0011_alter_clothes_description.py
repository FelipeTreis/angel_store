# Generated by Django 4.0.5 on 2022-08-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angel', '0010_alter_clothes_author_alter_clothes_brands_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothes',
            name='description',
            field=models.TextField(verbose_name='Descrição'),
        ),
    ]

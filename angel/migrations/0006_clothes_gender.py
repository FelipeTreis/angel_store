# Generated by Django 4.0.5 on 2022-07-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angel', '0005_alter_clothes_qty_parcel'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unisex')], default='U', max_length=1),
        ),
    ]

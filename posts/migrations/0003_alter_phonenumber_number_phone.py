# Generated by Django 4.1.3 on 2022-11-21 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='number_phone',
            field=models.CharField(max_length=20),
        ),
    ]

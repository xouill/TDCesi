# Generated by Django 2.1.5 on 2019-02-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190213_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concert',
            name='groupe',
        ),
        migrations.AlterField(
            model_name='placevendu',
            name='place',
            field=models.CharField(max_length=200),
        ),
    ]
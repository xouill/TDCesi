# Generated by Django 2.1.5 on 2019-03-12 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placevendu',
            name='place',
            field=models.ForeignKey(default=-1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='TypePlaceVendu', to='app.TypePlace'),
        ),
    ]
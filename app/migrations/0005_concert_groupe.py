# Generated by Django 2.1.5 on 2019-02-13 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_concert_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='groupe',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Groupe', to='app.Groupe'),
        ),
    ]

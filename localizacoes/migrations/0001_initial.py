# Generated by Django 3.2.3 on 2021-05-20 18:00

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ponto_loc', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, help_text='Point(longitude latitude)', null=True, srid=4326)),
            ],
        ),
    ]

# Generated by Django 5.0.4 on 2025-01-20 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appn1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'wrost'), (2, 'bad'), (3, 'average'), (4, 'good'), (5, 'excellent')]),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-27 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_tournamentmatch_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='players',
            field=models.CharField(max_length=1500),
        ),
    ]

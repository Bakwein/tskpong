# Generated by Django 5.0.3 on 2024-04-23 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_friends_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='name',
            field=models.CharField(default=datetime.datetime(2024, 4, 23, 14, 23, 11, 336597, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-23 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_royal_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='description',
            field=models.TextField(default=datetime.datetime(2023, 6, 23, 15, 20, 9, 83359, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2023-02-19 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Join_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]

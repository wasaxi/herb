# Generated by Django 3.1.1 on 2020-10-20 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201011_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixlist',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 20, 14, 24, 14, 649603)),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 20, 14, 24, 14, 645614)),
        ),
    ]

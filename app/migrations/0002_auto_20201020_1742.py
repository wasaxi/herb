# Generated by Django 3.0.3 on 2020-10-20 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='data',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='camera',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='camera',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 20, 17, 42, 3, 520050)),
        ),
        migrations.AlterField(
            model_name='camera',
            name='state',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='fixlist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='fixlist',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 20, 17, 42, 3, 525066)),
        ),
        migrations.AlterField(
            model_name='humiditysensor',
            name='data',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='humiditysensor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='humiditysensor',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 20, 17, 42, 3, 520050)),
        ),
        migrations.AlterField(
            model_name='humiditysensor',
            name='state',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='incubator',
            name='incubator_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='incubator',
            name='state',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='incubatorhistory',
            name='curTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 20, 17, 42, 3, 525066)),
        ),
        migrations.AlterField(
            model_name='incubatorhistory',
            name='humidity',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='incubatorhistory',
            name='light',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='incubatorhistory',
            name='plant',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='incubatorhistory',
            name='pressure',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='incubatorhistory',
            name='temperature',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='lightsensor',
            name='data',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='lightsensor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lightsensor',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 20, 17, 42, 3, 520050)),
        ),
        migrations.AlterField(
            model_name='lightsensor',
            name='state',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='plant',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='plant',
            name='img',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='mark',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='state',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='pressuresensor',
            name='data',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='pressuresensor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pressuresensor',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 20, 17, 42, 3, 520050)),
        ),
        migrations.AlterField(
            model_name='pressuresensor',
            name='state',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='temperaturesensor',
            name='data',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='temperaturesensor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='temperaturesensor',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 20, 17, 42, 3, 520050)),
        ),
        migrations.AlterField(
            model_name='temperaturesensor',
            name='state',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastLoginTime',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 20, 17, 42, 3, 520050)),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 20, 17, 42, 3, 520050)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

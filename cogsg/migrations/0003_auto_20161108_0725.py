# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-08 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cogsg', '0002_auto_20161108_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('Attend_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Create_Date', models.DateTimeField(auto_now_add=True)),
                ('Lords_Table', models.BooleanField(default=True)),
                ('Prayer_Meeting', models.BooleanField(default=True)),
                ('Morning_Revival', models.BooleanField(default=True)),
                ('Bible_Reading', models.BooleanField(default=True)),
                ('Small_Group', models.BooleanField(default=True)),
                ('Member_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Attend', to='cogsg.Member')),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.RemoveField(
            model_name='attendhistory',
            name='Member_ID',
        ),
        migrations.DeleteModel(
            name='AttendHistory',
        ),
    ]
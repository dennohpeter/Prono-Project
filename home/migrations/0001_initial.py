# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-19 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Prono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=40)),
                ('match_date', models.CharField(max_length=40)),
                ('time', models.CharField(max_length=40)),
                ('teams', models.CharField(max_length=400)),
                ('prob1', models.CharField(max_length=40)),
                ('probX', models.CharField(max_length=40)),
                ('prob2', models.CharField(max_length=40)),
                ('chance', models.CharField(max_length=40)),
                ('odd1', models.CharField(max_length=40)),
                ('oddX', models.CharField(max_length=40)),
                ('odd2', models.CharField(max_length=40)),
                ('win_odd', models.CharField(max_length=20)),
                ('match_result', models.CharField(max_length=40)),
                ('result_home', models.CharField(max_length=10)),
                ('result_away', models.CharField(max_length=10)),
                ('result_overall', models.CharField(max_length=20)),
            ]
        )
    ]

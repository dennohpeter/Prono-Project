# Generated by Django 2.2.4 on 2019-11-04 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191104_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allgames',
            old_name='result',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='featured',
            old_name='result',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='over15',
            old_name='result',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='over25',
            old_name='result',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='over35',
            old_name='result',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='tipgg',
            old_name='result',
            new_name='score',
        ),
    ]
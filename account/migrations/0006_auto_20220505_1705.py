# Generated by Django 3.2.8 on 2022-05-05 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20220505_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='action',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='is_block',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='publish',
        ),
    ]

# Generated by Django 3.2.8 on 2022-05-05 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]

# Generated by Django 3.2.8 on 2022-05-06 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20220506_0958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-publish_on',)},
        ),
        migrations.AlterField(
            model_name='blog',
            name='publish_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 5, 6, 10, 38, 15, 342100), null=True),
        ),
    ]

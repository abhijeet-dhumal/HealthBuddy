# Generated by Django 3.2.8 on 2022-05-06 10:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20220506_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_on',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]

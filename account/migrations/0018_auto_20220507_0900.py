# Generated by Django 3.2.8 on 2022-05-07 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_alter_review_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='feedback',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

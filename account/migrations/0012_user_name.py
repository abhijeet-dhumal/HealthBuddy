# Generated by Django 3.2.8 on 2022-05-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_remove_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='User', max_length=200),
        ),
    ]
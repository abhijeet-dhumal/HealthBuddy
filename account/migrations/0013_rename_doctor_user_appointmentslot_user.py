# Generated by Django 3.2.8 on 2022-05-06 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointmentslot',
            old_name='doctor_user',
            new_name='user',
        ),
    ]

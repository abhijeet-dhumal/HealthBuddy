# Generated by Django 3.2.8 on 2022-05-06 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_rename_doctor_user_appointmentslot_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='patient_user',
            new_name='user',
        ),
    ]

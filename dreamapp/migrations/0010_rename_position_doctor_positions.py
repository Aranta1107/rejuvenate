# Generated by Django 4.1.3 on 2022-11-09 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dreamapp', '0009_remove_doctor_doctor_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='position',
            new_name='positions',
        ),
    ]
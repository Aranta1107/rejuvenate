# Generated by Django 4.1.3 on 2022-11-07 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dreamapp', '0004_rename_number_of_integers_department_number_of_doctors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='department_id',
            new_name='department_name',
        ),
    ]
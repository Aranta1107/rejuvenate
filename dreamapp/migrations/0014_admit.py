# Generated by Django 4.1.3 on 2022-11-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreamapp', '0013_alter_appointment_apppointment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.TextField()),
                ('admit_date', models.DateField()),
            ],
        ),
    ]

# Generated by Django 5.0 on 2024-01-14 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_booking_id_alter_booking_no_of_guests_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuItem',
            new_name='Menu',
        ),
    ]
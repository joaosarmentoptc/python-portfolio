# Generated by Django 4.2.4 on 2023-08-18 23:00

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_alter_employee_personal_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='residential_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-19 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_remove_employee_supervisor_employee_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
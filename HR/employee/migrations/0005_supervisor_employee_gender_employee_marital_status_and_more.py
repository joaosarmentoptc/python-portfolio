# Generated by Django 4.2.4 on 2023-08-19 11:46

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_residential_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('D', 'Direct'), ('F', 'Functional')], default=None, max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=None, max_length=1),
        ),
        migrations.AddField(
            model_name='employee',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('MARRIED', 'Married'), ('SINGLE', 'Single'), ('DIVORCED', 'Divorced'), ('WIDOWED', 'Widowed'), ('PARTNERSHIP', 'Partnership')], default=None, max_length=15),
        ),
        migrations.AddField(
            model_name='employee',
            name='nationality',
            field=django_countries.fields.CountryField(default='PT', max_length=2),
        ),
        migrations.AddField(
            model_name='employee',
            name='residential_country',
            field=django_countries.fields.CountryField(default='PT', max_length=2),
        ),
        migrations.AddField(
            model_name='employee',
            name='supervisor',
            field=models.ManyToManyField(related_name='supervises', through='employee.Supervisor', to='employee.employee'),
        ),
    ]
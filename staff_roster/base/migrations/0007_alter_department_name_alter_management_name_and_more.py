# Generated by Django 4.2.4 on 2023-08-19 08:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_employee_department_alter_employee_management_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_numeric_name', message='Название должно содержать только цифры.', regex='^\\d+$')]),
        ),
        migrations.AlterField(
            model_name='management',
            name='name',
            field=models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_numeric_name', message='Название должно содержать только цифры.', regex='^\\d+$')]),
        ),
        migrations.AlterField(
            model_name='sector',
            name='name',
            field=models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_numeric_name', message='Название должно содержать только цифры.', regex='^\\d+$')]),
        ),
    ]

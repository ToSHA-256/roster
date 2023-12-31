# Generated by Django 4.2.4 on 2023-08-19 08:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_department_name_alter_management_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator(code='invalid_numeric_name', message='Название должно содержать только цифры.', regex='^\\d+$')]),
        ),
    ]

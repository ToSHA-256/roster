# Generated by Django 4.2.4 on 2023-08-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_department_options_alter_management_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_manager_department',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_manager_management',
            field=models.BooleanField(default=False),
        ),
    ]

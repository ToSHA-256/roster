# Generated by Django 4.2.4 on 2023-08-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_department_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_user',
            field=models.BooleanField(default=False),
        ),
    ]
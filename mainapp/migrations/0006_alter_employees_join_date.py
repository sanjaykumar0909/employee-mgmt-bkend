# Generated by Django 5.0.2 on 2024-02-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_employees_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='join_date',
            field=models.DateField(),
        ),
    ]
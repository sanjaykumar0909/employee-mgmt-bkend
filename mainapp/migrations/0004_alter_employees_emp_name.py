# Generated by Django 5.0.2 on 2024-02-28 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_employees_dob_alter_employees_emp_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='emp_name',
            field=models.CharField(max_length=50),
        ),
    ]

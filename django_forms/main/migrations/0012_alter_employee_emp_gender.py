# Generated by Django 5.0.6 on 2024-05-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_employee_emp_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True),
        ),
    ]
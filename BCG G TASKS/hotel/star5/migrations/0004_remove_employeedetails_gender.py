# Generated by Django 4.1.7 on 2023-02-28 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('star5', '0003_employeedetails_delete_empdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='gender',
        ),
    ]
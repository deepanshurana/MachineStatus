# Generated by Django 2.2.3 on 2020-01-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machineApp', '0002_mod_updateddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod',
            name='data',
            field=models.CharField(default={}, max_length=270),
        ),
    ]

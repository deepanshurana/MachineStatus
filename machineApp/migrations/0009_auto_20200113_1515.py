# Generated by Django 2.2.3 on 2020-01-13 15:15

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machineApp', '0008_auto_20200113_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]

# Generated by Django 2.2.3 on 2020-01-13 14:45

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('machineApp', '0004_auto_20200113_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod',
            name='data',
            field=jsonfield.fields.JSONField(blank=True, max_length=270),
        ),
    ]

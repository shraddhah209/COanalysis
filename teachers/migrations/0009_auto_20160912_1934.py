# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0008_auto_20160912_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_roll',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-02-02 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pis_com', '0008_customer_person_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='person_type',
            field=models.CharField(blank=True, default='customer', max_length=200, null=True),
        ),
    ]
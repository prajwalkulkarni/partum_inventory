# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-08 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pis_com', '0006_auto_20180604_2203'),
        ('pis_product', '0007_claimedproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='claimedproduct',
            name='claimed_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='claimedproduct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='claimedproduct',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_claimed_items', to='pis_com.Customer'),
        ),
        migrations.AddField(
            model_name='claimedproduct',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
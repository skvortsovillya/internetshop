# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(default=None, upload_to='product_img/'),
        ),
    ]

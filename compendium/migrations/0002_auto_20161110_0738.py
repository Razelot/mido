# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-10 07:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compendium', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demon',
            name='level_max',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='demon',
            name='level_min',
            field=models.IntegerField(default=99, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)]),
        ),
    ]

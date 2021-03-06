# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 14:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('microposts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('micropost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='microposts.Micropost')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-29 05:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.TextField(max_length=30)),
                ('classYear', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.TextField(max_length=30)),
                ('studentYear', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('studentDept', models.TextField(max_length=20)),
                ('studentClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentMgmtApp.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherName', models.TextField(max_length=30)),
                ('teacherDept', models.TextField(max_length=20)),
                ('teacherClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentMgmtApp.Class')),
            ],
        ),
    ]
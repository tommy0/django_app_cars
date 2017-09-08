# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 23:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarCareer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('mass', models.IntegerField()),
                ('overload', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(choices=[('\u0411\u0435\u043b\u0430\u0437', '\u0411\u0435\u043b\u0430\u0437'), ('Komatsu', 'Komatsu')], max_length=100)),
                ('mass', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='carcareer',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.CarModel'),
        ),
    ]
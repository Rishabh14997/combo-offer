# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coderun', '0002_auto_20170828_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='model1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('upper_limit', models.PositiveIntegerField()),
                ('lower_limit', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=70)),
            ],
        ),
        migrations.RemoveField(
            model_name='code',
            name='email',
        ),
        migrations.RemoveField(
            model_name='code',
            name='file',
        ),
        migrations.AddField(
            model_name='model1',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coderun.Code'),
        ),
    ]

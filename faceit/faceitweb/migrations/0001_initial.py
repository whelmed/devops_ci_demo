# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 16:32
from __future__ import unicode_literals

from django.db import migrations, models

def seed_initial_user_names(apps, schema_editor):
    User = apps.get_model("faceitweb", "User")
    for name in ['John Smith', 'Marth Jones', 'Rose Tyler', 'Sarah Jane Smith', 'Donna Noble']:

        User(full_name=name).save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.RunPython(seed_initial_user_names),
    ]

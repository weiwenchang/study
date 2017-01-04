# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_info1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=16)),
                ('ugender', models.BooleanField()),
                ('ueamil', models.CharField(max_length=20)),
                ('utell', models.CharField(max_length=11)),
                ('uaddress', models.CharField(max_length=40)),
                ('isDelete', models.BooleanField()),
            ],
        ),
    ]

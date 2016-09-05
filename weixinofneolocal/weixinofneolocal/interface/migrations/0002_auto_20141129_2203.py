# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='msgrecord',
            name='event',
            field=models.CharField(default=b'', max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='msgrecord',
            name='picmd5',
            field=models.CharField(default=b'', max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='msgrecord',
            name='picount',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mediamsg',
            name='filefd',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='msgrecord',
            name='msgid',
            field=models.BigIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='msgrecord',
            name='msgtime',
            field=models.IntegerField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]

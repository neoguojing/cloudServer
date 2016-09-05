# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0002_auto_20141129_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScanCode',
            fields=[
                ('msgtime', models.IntegerField(serialize=False, primary_key=True)),
                ('msgtype', models.CharField(default=b'', max_length=30, blank=True)),
                ('event', models.CharField(default=b'', max_length=30, blank=True)),
                ('eventkey', models.CharField(default=b'', max_length=50, blank=True)),
                ('scantype', models.CharField(default=b'', max_length=30, blank=True)),
                ('scanresult', models.CharField(default=b'', max_length=200, blank=True)),
                ('tickit', models.CharField(default=b'', max_length=100, blank=True)),
                ('userid', models.ForeignKey(to='interface.WeiXinUsers')),
            ],
            options={
                'ordering': ['userid', 'msgtime'],
            },
            bases=(models.Model,),
        ),
    ]

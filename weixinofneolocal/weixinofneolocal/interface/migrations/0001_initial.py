# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemOfNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.IntegerField()),
                ('title', models.CharField(max_length=50, blank=True)),
                ('description', models.TextField(blank=True)),
                ('pic_url', models.URLField(blank=True)),
                ('url', models.URLField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LocationOfUser',
            fields=[
                ('msgtime', models.IntegerField(serialize=False, primary_key=True)),
                ('msgid', models.BigIntegerField(default=0, blank=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('precision', models.FloatField(default=0.0, blank=True)),
                ('scale', models.IntegerField(default=0, blank=True)),
                ('lable', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'ordering': ['userid', 'msgtime'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MediaMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=30)),
                ('msgtype', models.CharField(max_length=10)),
                ('isactive', models.BooleanField()),
                ('mediaid', models.CharField(max_length=200)),
                ('filefd', models.FileField(upload_to=b'image/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MsgRecord',
            fields=[
                ('msgid', models.BigIntegerField(serialize=False, primary_key=True)),
                ('msgtime', models.IntegerField()),
                ('msgtype', models.CharField(max_length=30)),
                ('eventkey', models.CharField(max_length=50, blank=True)),
                ('title', models.CharField(max_length=50, blank=True)),
                ('content', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('mediaid', models.CharField(max_length=200)),
                ('thumediaid', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['userid', 'msgtime'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MusicMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=30)),
                ('isactive', models.BooleanField()),
                ('title', models.CharField(max_length=50, blank=True)),
                ('desc', models.TextField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('hqurl', models.URLField(blank=True)),
                ('mediaid', models.CharField(max_length=200)),
                ('filefd', models.FileField(upload_to=b'music/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('key', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('isactive', models.BooleanField()),
                ('itemcount', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=30)),
                ('isactive', models.BooleanField()),
                ('text', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=30)),
                ('isactive', models.BooleanField()),
                ('title', models.CharField(max_length=50, blank=True)),
                ('desc', models.TextField(blank=True)),
                ('mediaid', models.CharField(max_length=200)),
                ('filefd', models.FileField(upload_to=b'video/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeiXinDeveloperInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appid', models.CharField(max_length=30)),
                ('secret', models.CharField(max_length=50)),
                ('access_token', models.CharField(max_length=50, blank=True)),
                ('token', models.CharField(max_length=10)),
                ('weixinid', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeiXinGroups',
            fields=[
                ('gid', models.IntegerField(serialize=False, primary_key=True)),
                ('gname', models.CharField(max_length=30, blank=True)),
                ('count', models.IntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeiXinUsers',
            fields=[
                ('userid', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('issubscribe', models.BooleanField()),
                ('nickname', models.CharField(max_length=30, blank=True)),
                ('sex', models.BooleanField()),
                ('city', models.CharField(max_length=30, blank=True)),
                ('country', models.CharField(max_length=30, blank=True)),
                ('province', models.CharField(max_length=30, blank=True)),
                ('language', models.CharField(max_length=10, blank=True)),
                ('headimgurl', models.URLField(blank=True)),
                ('subscribe_time', models.IntegerField(blank=True)),
                ('unionid', models.CharField(max_length=50, blank=True)),
                ('gid', models.ForeignKey(related_name='user_set', to='interface.WeiXinGroups')),
            ],
            options={
                'ordering': ['gid', 'nickname'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='videomsg',
            name='userid',
            field=models.ForeignKey(to='interface.WeiXinUsers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='musicmsg',
            name='userid',
            field=models.ForeignKey(to='interface.WeiXinUsers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='msgrecord',
            name='userid',
            field=models.ForeignKey(to='interface.WeiXinUsers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediamsg',
            name='userid',
            field=models.ForeignKey(to='interface.WeiXinUsers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='locationofuser',
            name='userid',
            field=models.ForeignKey(to='interface.WeiXinUsers'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='itemofnews',
            name='item',
            field=models.ForeignKey(related_name='item_set', to='interface.News'),
            preserve_default=True,
        ),
    ]

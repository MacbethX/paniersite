# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20140911_0405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac', models.CharField(max_length=100, verbose_name=b'meter mac')),
                ('transformer', models.CharField(max_length=100, verbose_name=b'meter transformer')),
                ('longitute', models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

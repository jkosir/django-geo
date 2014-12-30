# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_location_iata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrativearea',
            name='country',
            field=models.ForeignKey(related_name='areas', to='geo.Country'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='administrativearea',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='areas', default=None, blank=True, to='geo.AdministrativeArea', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='administrativeareatype',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='geo.AdministrativeAreaType', null=True),
            preserve_default=True,
        ),
    ]

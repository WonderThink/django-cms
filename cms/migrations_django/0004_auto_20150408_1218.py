# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsplugin',
            name='plugin_type',
            field=models.CharField(verbose_name='plugin name', max_length=50, editable=False, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='title',
            name='has_url_overwrite',
            field=models.BooleanField(default=False, verbose_name='has URL overwrite', db_index=True, editable=False),
            preserve_default=True,
        ),
    ]

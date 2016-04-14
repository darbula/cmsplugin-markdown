# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_markdown', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markdownplugin',
            name='markdown_text',
            field=models.TextField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_messages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='doc_file',
            field=models.FileField(upload_to=b'uploaded/doc_file/%Y/%m/%d/', max_length=255, verbose_name='Document file', blank=True),
            preserve_default=True,
        ),
    ]

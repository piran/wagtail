# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0015_genericsnippetpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customimage',
            name='uploaded_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='Uploaded by user'),
        ),
    ]

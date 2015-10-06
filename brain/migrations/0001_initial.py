# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('tag', models.TextField(null=True, editable=False, blank=True)),
                ('owner', models.CharField(db_index=True, max_length=100, null=True, editable=False, blank=True)),
                ('classification', models.TextField(db_index=True)),
                ('content', models.TextField(db_index=True, null=True, blank=True)),
            ],
        ),
    ]

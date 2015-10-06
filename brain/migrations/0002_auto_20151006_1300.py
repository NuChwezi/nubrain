# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('tag', models.TextField(null=True, editable=False, blank=True)),
                ('owner', models.CharField(db_index=True, max_length=100, null=True, editable=False, blank=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
            ],
            options={
                'verbose_name': 'Classification',
                'verbose_name_plural': 'Classifications',
            },
        ),
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name': 'Data', 'verbose_name_plural': 'Data'},
        ),
        migrations.RemoveField(
            model_name='data',
            name='classification',
        ),
        migrations.AddField(
            model_name='data',
            name='classification',
            field=models.ManyToManyField(related_name='my_data', to='brain.Classification'),
        ),
    ]

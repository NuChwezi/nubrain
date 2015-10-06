from django.db import models
from brain.utils import text_snippet_start


class Classification(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tag = models.TextField(editable=False, null=True, blank=True)
    owner = models.CharField(
        max_length=100, db_index=True, editable=False, null=True, blank=True)

    name = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Classification'
        verbose_name_plural = 'Classifications'


class Data(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    tag = models.TextField(editable=False, null=True, blank=True)
    owner = models.CharField(
        max_length=100, db_index=True, editable=False, null=True, blank=True)

    classification = models.ManyToManyField(Classification, related_name='my_data')
    content = models.TextField(null=True, blank=True, db_index=True)

    def __unicode__(self):
        return self.get_preview()

    def get_preview(self):
        return text_snippet_start(self.content, max_len=10)
    get_preview.short_description = 'Preview'

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Data'

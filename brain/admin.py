from django.contrib import admin
from brain.models import Data, Classification


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Classification, ClassificationAdmin)


class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_update', 'view_classification', 'get_preview',)
    search_fields = ('classification__name', 'content', )
    list_filter = ('classification',)

    def view_classification(self, obj):
        if obj is not None:
            return '<a href="?" class="btn btn-default">.</a> ' + ' '.join(['<a href="?%(filter)s" class="btn btn-default">%(val)s</a>' % {'val': c.name, 'filter': 'classification__id__exact=%s' % c.id } for c in obj.classification.all()])
        else:
            return ''
    view_classification.short_description = 'Classification'
    view_classification.allow_tags = True


admin.site.register(Data, DataAdmin)

from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *

class ValueResource(resources.ModelResource):
    class Meta:
        model = Value

class ValueAdmin(ImportExportModelAdmin):
    resource_class = ValueResource



class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language

class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource



class ValueLinkResource(resources.ModelResource):
    class Meta:
        model = ValueLink

class ValueLinkAdmin(ImportExportModelAdmin):
    resource_class = ValueLinkResource


admin.site.register(Value, ValueAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(ValueLink, ValueLinkAdmin)
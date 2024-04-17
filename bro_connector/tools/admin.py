from reversion_compare.helpers import patch_admin 
from django.db import models
from django.contrib import admin
from django.db.models import fields
from reversion_compare.helpers import patch_admin 
from . import models as tools_models

def _register(model, admin_class):
    admin.site.register(model, admin_class)

def get_searchable_fields(model_class: models.Model) -> list[str]:
    return [
        f.name
        for f in model_class._meta.fields
        if isinstance(f, (fields.CharField, fields.AutoField))
    ]

class BroImporterAdmin(admin.ModelAdmin):
    search_fields = get_searchable_fields(tools_models.BroImporter)

    list_display = (
        "id",
        "bro_type",
        "kvk_number",
        "import_date",
    )

    list_filter = (
        "bro_type",
        "kvk_number",
    )

    readonly_fields = ('import_date', "created_date",)

    actions = ["update_import"]

    def save_model(self, request, obj, form, change):
        pass

    @admin.action(description="Re-import values from the BRO.")
    def update_import(self, request, queryset):
        pass

_register(tools_models.BroImporter, BroImporterAdmin)
patch_admin(tools_models.BroImporter)
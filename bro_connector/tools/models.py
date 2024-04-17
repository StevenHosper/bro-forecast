from django.db import models
import datetime
from .choices import *

class BroImporter(models.Model):
    bro_type = models.CharField(choices=BRO_TYPES, null=False)
    kvk_number = models.IntegerField(max_length=25, null=False)
    import_date = models.DateTimeField(editable=False, default=datetime.datetime.now())

    class Meta:
        managed = True
        db_table = 'tools"."bro_importer'
        verbose_name = "Importer"
        verbose_name_plural = "BRO Importer"
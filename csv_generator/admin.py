from django.contrib import admin
from csv_generator.models import Schema, Column, DataSet

# Register your models here.
admin.site.register(Schema)
admin.site.register(Column)
admin.site.register(DataSet)


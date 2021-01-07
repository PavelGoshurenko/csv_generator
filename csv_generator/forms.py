from django import forms
from django.forms import ModelForm, Select, NumberInput
from csv_generator.models import Schema, DataSet, Column


class SchemaForm (forms.ModelForm):
    class Meta:
        model = Schema
        fields = ('name', 'separator', 'string_character')

class DataSetForm (forms.ModelForm):
    class Meta:
        model = DataSet
        fields = ('rows',)

class ColumnForm (forms.ModelForm):
    class Meta:
        model = Column
        fields = ('name', 'data_type', 'start_from', 'to', 'order')
        widgets = {
            'data_type': Select(attrs={"onchange": "showRange(event)"}),
            'start_from': NumberInput(attrs={"hidden": "true"}),
            'to': NumberInput(attrs={"hidden": "true"}),
        }


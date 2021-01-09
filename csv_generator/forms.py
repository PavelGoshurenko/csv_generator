from django import forms
from django.forms import Select, NumberInput
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
    '''The form adds JS handler function for the 'data_type' field. (The function itself is in the template add_schema.html).
    For 'start_from' and  'to' fields, the "hidden" attribute is added. This attribute will also be changed in the template using JS functions.'''
    class Meta:
        model = Column
        fields = ('name', 'data_type', 'start_from', 'to', 'order')
        widgets = {
            'data_type': Select(attrs={"onchange": "showRange(event)"}),
            'start_from': NumberInput(attrs={"hidden": "true"}),
            'to': NumberInput(attrs={"hidden": "true"}),
        }

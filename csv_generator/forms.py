from django import forms
from django.forms import ModelForm
from csv_generator.models import Schema


class SchemaForm (forms.ModelForm):
    class Meta:
        model = Schema
        fields = ('name',)


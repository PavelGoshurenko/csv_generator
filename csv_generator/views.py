from django.shortcuts import render
from django.views import generic
from django.forms.models import inlineformset_factory
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from csv_generator.models import Schema, Column

# Schemas views
class SchemasView(generic.ListView):
    template_name = 'schemas.html'
    context_object_name = 'schemas'

    def get_queryset(self):
        return Schema.objects.all()


class SchemaView(generic.DetailView):
    model = Schema
    template_name = "schema.html"


class SchemaCreate(CreateView):
    model = Schema
    fields = ['name']
    success_url = reverse_lazy('schemas')

    def get_context_data(self, **kwargs):
        context = super(SchemaCreate, self).get_context_data(**kwargs)
        ColumnsFormSet = inlineformset_factory(Schema, Column, exclude=('id',))
        context['formset'] = ColumnsFormSet()
        return context


class SchemaUpdate(UpdateView):
    model = Schema
    fields = '__all__'
    success_url = reverse_lazy('schemas')
    template_name = 'schema_update.html'


class SchemaDelete(DeleteView):
    model = Schema
    success_url = reverse_lazy('schemas')
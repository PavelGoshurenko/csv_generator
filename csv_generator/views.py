from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.forms.models import inlineformset_factory
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from csv_generator.models import Schema, Column, DataSet
from csv_generator.forms import SchemaForm, DataSetForm, ColumnForm
from csv_generator.tasks import generate_csv


class SchemasView(LoginRequiredMixin, generic.ListView):
    template_name = 'schemas.html'
    context_object_name = 'schemas'

    def get_queryset(self):
        return Schema.objects.filter(user=self.request.user)


@login_required
def schema_create(request):
    '''Creates a new schema and a set of columns for it.'''
    ColumnsFormSet = inlineformset_factory(
        Schema,
        Column,
        form=ColumnForm,
        can_order=False,
        extra=1,
        can_delete=False)
    if request.method == 'POST':
        formset = ColumnsFormSet(request.POST)
        form = SchemaForm(request.POST)
        if formset.is_valid() and form.is_valid():
            schema = form.save()
            schema.user = request.user
            schema.save()
            for column_form in formset:
                if column_form.cleaned_data:
                    column = column_form.save(commit=False)
                    column.schema = schema
                    column.save()
            return redirect('schemas')
        else:
            return render(
                request,
                'add_schema.html',
                {'formset': formset, 'form': form})
    else:
        formset = ColumnsFormSet()
        form = SchemaForm()
    return render(
        request,
        'add_schema.html',
        {'formset': formset, 'form': form}
    )


class SchemaDelete(LoginRequiredMixin, DeleteView):
    model = Schema
    success_url = reverse_lazy('schemas')


@login_required
def data_sets(request, pk):
    '''Displays all datasets for the schema. Generates csv files for datasets.'''
    schema = Schema.objects.get(id=pk)
    if request.method == 'POST':
        form = DataSetForm(request.POST)
        if form.is_valid():
            new_data_set = DataSet(
                rows=form.cleaned_data['rows'],
                schema=schema
            )
            new_data_set.save()
            generate_csv.delay(new_data_set.id) # Send generate csv file task to celery.
    form = DataSetForm()
    data_sets = DataSet.objects.filter(schema=schema)
    return render(
        request,
        'data_sets.html',
        {
            'schema': schema,
            'data_sets': data_sets,
            'form': form
        }
    )

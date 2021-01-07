from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.forms.models import inlineformset_factory
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from csv_generator.models import Schema, Column, DataSet
from csv_generator.forms import SchemaForm, DataSetForm, ColumnForm
from csv_generator.tasks import generate_csv


# delete
import csv
import random
import os
from faker import Faker
import time
from io import StringIO
from os.path import join
from django.conf import settings
from django.core.files.base import ContentFile
fake = Faker()



GENERATORS = {
    'Full name': fake.name,
    'Job': fake.job,
    'Address': fake.address,
    'Phone number': fake.phone_number,
}
########################

class SchemasView(LoginRequiredMixin, generic.ListView):
    template_name = 'schemas.html'
    context_object_name = 'schemas'

    def get_queryset(self):
        return Schema.objects.filter(user=self.request.user)


@login_required
def schema_create(request):
    ColumnsFormSet = inlineformset_factory(Schema, Column, form=ColumnForm, can_order=False, extra=1, can_delete=False)
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
        else: return render(request, 'add_schema.html', {'formset': formset, 'form': form})
    else:
        formset = ColumnsFormSet()
        form =  SchemaForm()
    return render(request, 'add_schema.html', {'formset': formset, 'form': form})



class SchemaDelete(LoginRequiredMixin, DeleteView):
    model = Schema
    success_url = reverse_lazy('schemas')

def generate_csvvv(data_set_id):
    data_set = DataSet.objects.get(id=data_set_id)
    schema = data_set.schema
    columns = Column.objects.filter(schema=schema).order_by('order')
    column_names = [column.name for column in columns]
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer, dialect='excel', delimiter=',', quotechar='"')
    writer.writerow(column_names)
    for _ in range(data_set.rows):
        row = []
        for column in columns:
            if column.data_type == "Age":
                row.append(random.randint(column.start_from, column.to))
            else:
                row.append(GENERATORS[column.data_type]())
        writer.writerow(row)
        time.sleep(1)
    csv_file = ContentFile(csv_buffer.getvalue().encode('utf-8'))
    file_name = '{}_{}.csv'.format(schema.name, data_set.created_at.strftime("%d_%m_%Y"))
    data_set.file.save(file_name, csv_file)
    data_set.status = 'Ready'
    data_set.save()

@login_required
def data_sets(request, pk):
    schema = Schema.objects.get(id=pk)
    if request.method == 'POST':
        form = DataSetForm(request.POST)
        if form.is_valid():
            new_data_set = DataSet(
                rows=form.cleaned_data['rows'],
                schema=schema
            )
            new_data_set.save()
            generate_csvvv(new_data_set.id) # add delay
    form = DataSetForm()
    data_sets = DataSet.objects.filter(schema=schema)
    return render(request, 'data_sets.html', {'schema': schema, 'data_sets': data_sets, 'form': form})


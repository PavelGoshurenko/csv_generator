from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.forms.models import inlineformset_factory
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from csv_generator.models import Schema, Column
from csv_generator.forms import SchemaForm

# Schemas views
class SchemasView(LoginRequiredMixin, generic.ListView):
    template_name = 'schemas.html'
    context_object_name = 'schemas'

    def get_queryset(self):
        return Schema.objects.all()


class SchemaView(LoginRequiredMixin, generic.DetailView):
    model = Schema
    template_name = "schema.html"


@login_required
def schema_create(request):
    ColumnsFormSet = inlineformset_factory(Schema, Column, can_order=False, extra=1, can_delete=False, exclude=('id',))
    if request.method == 'POST':
        formset = ColumnsFormSet(request.POST)
        form = SchemaForm(request.POST)
        if formset.is_valid() and form.is_valid():
            schema = form.save()
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



class SchemaUpdate(LoginRequiredMixin, UpdateView):
    model = Schema
    fields = '__all__'
    success_url = reverse_lazy('schemas')
    template_name = 'schema_update.html'


class SchemaDelete(LoginRequiredMixin, DeleteView):
    model = Schema
    success_url = reverse_lazy('schemas')
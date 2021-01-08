from django.urls import path
from csv_generator import views

urlpatterns = [
    path(
        '',
        views.SchemasView.as_view(),
        name='schemas'),
    path(
        'schema/<int:pk>/',
        views.data_sets,
        name='data_sets'),
    path(
        'schema/create/',
        views.schema_create,
        name='schema_create'),
    path(
        'schema/<int:pk>/delete/',
        views.SchemaDelete.as_view(),
        name='schema_delete'
        ),
]

from django.contrib import admin
from django.urls import path
from csv_generator import views

urlpatterns = [
    # schemas
    path('', views.SchemasView.as_view(), name='schemas'),
    path('schema/<int:pk>/', views.SchemaView.as_view(), name='schema'),
    path('schema/create/', views.schema_create, name='schema_create'),
    path(
        'schema/<int:pk>/update/',
        views.SchemaUpdate.as_view(),
        name='schema_update'
        ),
    path(
        'schema/<int:pk>/delete/',
        views.SchemaDelete.as_view(),
        name='schema_delete'
        ),
]

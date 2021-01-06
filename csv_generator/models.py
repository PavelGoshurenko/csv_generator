from django.db import models
from django.contrib.auth.models import User


class DataType(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Data Type")
    
    def __str__(self):
        return self.name



class Schema(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Schema")
    updated_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']

class Column(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Column name")
    data_type = models.ForeignKey(
        DataType, null=True,
        on_delete=models.ProtectedError,
        verbose_name='Type'
        )
    order = models.IntegerField(
        verbose_name='Order',
        default=0
        )
    schema = models.ForeignKey(
        Schema, null=True,
        on_delete=models.CASCADE,
        verbose_name='Schema'
        )
    
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']
        unique_together = ['schema', 'order']

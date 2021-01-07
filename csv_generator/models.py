from django.db import models
from django.contrib.auth.models import User


class Schema(models.Model):
    SEPARATORS = [
        (',', 'Comma (,)'),
        (';', 'Semicolon (;)'),
        ('  ', 'Tab (   )')
    ]
    STRING_CHARACTERS = [
        ('"', 'Double-quote (")'),
        ("'", "Single-quote (')")
    ]
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Schema")
    updated_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True, blank=True)
    separator = models.CharField(
        max_length=2,
        choices=SEPARATORS,
        default=",",
        verbose_name="Column separator"
        )
    string_character = models.CharField(
        max_length=2,
        choices=STRING_CHARACTERS,
        default='"',
        verbose_name="String character"
        )
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated_at']

class Column(models.Model):
    DATA_TYPES = [
        ('Full name', 'Full name'),
        ('Job', 'Job'),
        ('Address', 'Address'),
        ('Phone number', 'Phone number'),
        ('Age', 'Age')
    ]
    name = models.CharField(
        max_length=200,
        unique=False,
        verbose_name="Column name")
    data_type = models.CharField(
        max_length=20,
        choices=DATA_TYPES,
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
    start_from = models.IntegerField(
        verbose_name='From',
        default=18
        )
    to = models.IntegerField(
        verbose_name='To',
        default=60
        )
    
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']
        unique_together = ['schema', 'order']

class DataSet(models.Model):
    STATUS_CHOICES = [
        ('Ready', 'Ready'),
        ('Processing', 'Processing'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Processing')
    created_at = models.DateTimeField(auto_now=True)
    schema = models.ForeignKey(
        Schema,
        on_delete=models.CASCADE,
        verbose_name='Schema'
        )
    rows = models.PositiveIntegerField(verbose_name='Rows', default=500)
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.schema.name, self.created_at.strftime("%d.%m.%Y"))
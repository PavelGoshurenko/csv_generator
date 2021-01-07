# Generated by Django 3.1.5 on 2021-01-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_generator', '0007_auto_20210106_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='data_type',
            field=models.CharField(choices=[('Full name', 'Full name'), ('Job', 'Job')], default='lkdf', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dataset',
            name='rows',
            field=models.PositiveIntegerField(default=500, verbose_name='Rows'),
        ),
    ]
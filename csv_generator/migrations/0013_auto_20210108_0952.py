# Generated by Django 3.1.5 on 2021-01-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_generator', '0012_auto_20210107_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='order',
            field=models.IntegerField(verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='schema',
            name='separator',
            field=models.CharField(choices=[(',', 'Comma (,)'), (';', 'Semicolon (;)')], default=',', max_length=2, verbose_name='Column separator'),
        ),
        migrations.AlterField(
            model_name='schema',
            name='string_character',
            field=models.CharField(choices=[('"', 'Double-quote (")'), ("'", "Single-quote (')")], default='"', max_length=2, verbose_name='String character'),
        ),
    ]
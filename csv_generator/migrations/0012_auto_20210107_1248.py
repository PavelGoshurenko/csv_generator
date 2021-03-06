# Generated by Django 3.1.5 on 2021-01-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_generator', '0011_auto_20210107_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='separator',
            field=models.CharField(choices=[(',', 'Comma (,)'), (';', 'Semicolon (;)'), ('  ', 'Tab (   )')], default=',', max_length=2, verbose_name='Column separator'),
        ),
        migrations.AddField(
            model_name='schema',
            name='string_character',
            field=models.CharField(choices=[('"', 'Double-quote (")'), ("'", "Single-quote (')"), ('  ', 'Tab (   )')], default='"', max_length=2, verbose_name='String character'),
        ),
    ]

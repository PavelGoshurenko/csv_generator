# Generated by Django 3.1.5 on 2021-01-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_generator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Column')),
            ],
        ),
        migrations.AddField(
            model_name='schema',
            name='columns',
            field=models.ManyToManyField(to='csv_generator.Column'),
        ),
    ]

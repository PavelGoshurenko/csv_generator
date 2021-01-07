# Generated by Django 3.1.5 on 2021-01-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_generator', '0010_auto_20210107_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='data_type',
            field=models.CharField(choices=[('Full name', 'Full name'), ('Job', 'Job'), ('Address', 'Address'), ('Phone number', 'Phone number'), ('Age', 'Age')], max_length=20),
        ),
    ]

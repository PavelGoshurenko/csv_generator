import csv
import random
import os
from faker import Faker
import time
from generator.celery import app
from io import StringIO
from os.path import join
from django.conf import settings
from django.core.files.base import ContentFile
from csv_generator.models import DataSet, Column, Schema

fake = Faker()

def age_generator(start_from, to):
    return random.randint(start_from, to)

GENERATORS = {
    'Full name': fake.name,
    'Job': fake.job,
    'Address': fake.address,
    'Phone number': fake.phone_number,
}
"""
#if settings.DEBUG:
#app.conf.update(BROKER_URL=os.environ['REDIS_URL'], CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])
    #app.conf.broker_url = 'redis://localhost:6379/0'
#else:
     app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL']) """

@app.task
def generate_csv(data_set_id):
    data_set = DataSet.objects.get(id=data_set_id)
    schema = data_set.schema
    columns = Column.objects.filter(schema=schema).order_by('order')
    column_names = [column.name for column in columns]
    csv_buffer = StringIO()
    writer = csv.writer(csv_buffer, dialect='excel', delimiter=',', quotechar='"')
    writer.writerow(column_names)
    for _ in range(data_set.rows):
        row = []
        for column in columns:
            if column.data_type == "Age":
                row.append(random.randint(column.start_from, column.to))
            else:
                row.append(GENERATORS[column.data_type]())
        writer.writerow(row)
        time.sleep(1)
    csv_file = ContentFile(csv_buffer.getvalue().encode('utf-8'))
    file_name = '{}_{}.csv'.format(schema.name, data_set.created_at.strftime("%d_%m_%Y"))
    path = join('media/', file_name)
    data_set.file.save(file_name, csv_file)
    data_set.status = 'Ready'
    data_set.save()
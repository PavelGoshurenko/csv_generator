web: gunicorn generator.wsgi --log-file -
worker: celery -A generator worker --loglevel=INFO
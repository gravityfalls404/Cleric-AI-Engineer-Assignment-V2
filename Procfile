web: gunicorn app:app
worker: celery -A task worker --loglevel=info

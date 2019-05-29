web: gunicorn temba.wsgi:application --threads=$WEB_THREADS --worker-class=gthread --preload --log-file -
worker: celery -A temba worker --beat -Q flows,msgs,handler,celery -c $WORKER_CONCURRENCY
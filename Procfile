web: gunicorn temba.wsgi:application --log-file -
worker: celery -A temba worker --beat -Q flows,msgs,handler,celery -c 4
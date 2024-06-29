release: bash -c "python manage.py migrate && python manage.py collectstatic --noinput"
web: gunicorn bankcode.wsgi --log-file -

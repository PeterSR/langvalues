#!/bin/bash

echo "Settings: $DJANGO_SETTINGS_MODULE"

python manage.py makemigrations
python manage.py migrate

gunicorn "$DJANGO_BASE.wsgi:application" \
    --workers 4 \
    --bind 0.0.0.0:$DJANGO_PORT \
    --log-file '-' \
    --access-logfile '-' \
    "$@"

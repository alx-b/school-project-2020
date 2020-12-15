#!/bin/sh

set -e

python manage.py collectstatic --noinput

gunicorn -b :8443 -w 1 app.wsgi

#! /bin/bash
modprobe bcm2835-v4l2
cd /app
./manage.py collectstatic --noinput
./manage.py migrate --noinput
uwsgi --ini /app/uwsgi.ini

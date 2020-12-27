#!/bin/sh

mkdir -p /home/flask/logs
touch /home/flask/logs/gunicorn.log
touch /home/flask/logs/gunicorn-access.log
touch /home/flask/logs/gunicorn-error.log
tail -n 0 -f /home/flask/logs/gunicorn*.log &

gunicorn "app:create_app()" \
         --bind 0.0.0.0:5000 \
         --workers 2 \
         --log-level=info \
         --log-file=/home/flask/logs/gunicorn.log \
         --access-logfile=/home/flask/logs/gunicorn-access.log \
         --error-logfile=/home/flask/logs/gunicorn-error.log

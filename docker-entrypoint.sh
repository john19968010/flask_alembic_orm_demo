#!/bin/sh

set -e

# If arguments are passed to docker, run them instead
if [ ! "$#" -gt 0 ]; then
  PYTHONPATH=/usr/src/app gunicorn --worker-class eventlet -w 1 app:app --timeout 120 --threads 1 -b 127.0.0.1:10009
fi

exec "$@"

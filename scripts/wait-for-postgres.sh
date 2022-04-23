#!/bin/sh
# wait-for-postgres.sh

until python3 -m manage check --database default; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

#!/bin/bash

echo "Esperando a PostgreSQL..."
while ! nc -z $DB_HOST 5432; do
  sleep 0.1
done
echo "PostgreSQL iniciado"

echo "Aplicando migraciones..."
python manage.py makemigrations
python manage.py migrate

echo "Iniciando servidor..."
exec "$@"
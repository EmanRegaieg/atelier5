#!/bin/sh

echo "📦 Applying database migrations..."
python manage.py migrate

echo "👤 Creating superuser (if not exists)..."
python manage.py createsuperuser --noinput || echo "Superuser already exists"

echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

echo "🚀 Starting Gunicorn..."
exec gunicorn monprojet.wsgi:application --bind 0.0.0.0:8000
#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies (from your requirements.txt)
pip install -r requirements.txt

# Create static files directory and collect static files
python manage.py collectstatic --no-input

# Run database migrations (Djongo only needs this once to create the collections)
python manage.py migrate
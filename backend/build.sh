#!/usr/bin/env bash
# exit on error
set -o errexit

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the backend directory (where this script is located)
cd "$SCRIPT_DIR"

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py populate_db 
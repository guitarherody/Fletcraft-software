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

# Run populate_db command if it exists, but don't fail if it doesn't
if python manage.py help populate_db > /dev/null 2>&1; then
    python manage.py populate_db
else
    echo "populate_db command not found, skipping..."
fi 
#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Building frontend..."
cd frontend

# Use npm ci if package-lock.json exists, otherwise use npm install
if [ -f "package-lock.json" ]; then
    echo "Found package-lock.json, using npm ci..."
    npm ci
else
    echo "No package-lock.json found, using npm install..."
    npm install
fi

npm run build 
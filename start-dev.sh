#!/bin/bash

echo "🚀 Starting FLETCRAFT SOFTWARE INC. Development Servers"

# Kill any existing processes on these ports
echo "🧹 Cleaning up existing processes..."
lsof -ti:8000 | xargs kill -9 2>/dev/null || true
lsof -ti:3000 | xargs kill -9 2>/dev/null || true
lsof -ti:3001 | xargs kill -9 2>/dev/null || true
lsof -ti:3002 | xargs kill -9 2>/dev/null || true

# Start Django backend
echo "🔧 Starting Django backend..."
cd backend
source venv/bin/activate
python manage.py runserver 8000 &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 2

# Start Svelte frontend
echo "🎨 Starting Svelte frontend..."
cd ../frontend
npm run dev &
FRONTEND_PID=$!

echo ""
echo "✅ Servers started successfully!"
echo "🌐 Frontend: http://localhost:3000/"
echo "🔧 Backend API: http://localhost:8000/api/"
echo "📊 Django Admin: http://localhost:8000/admin/"
echo ""
echo "Press Ctrl+C to stop all servers"

# Wait for user to stop
trap "echo '🛑 Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT
wait 
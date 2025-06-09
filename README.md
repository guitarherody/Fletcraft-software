# FLETCRAFT SOFTWARE INC. Website

A modern business website built with Django and Svelte.

## Project Structure
- `backend/` - Django backend server
- `frontend/` - Svelte frontend application

## Setup Instructions

### Backend Setup
1. Create a Python virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the Django server:
```bash
python manage.py runserver
```

### Frontend Setup
1. Install dependencies:
```bash
cd frontend
npm install
```

2. Start the development server:
```bash
npm run dev
```

## Development
- Backend runs on http://localhost:8000
- Frontend runs on http://localhost:5173 
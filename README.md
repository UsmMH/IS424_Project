# FitSync — Gym Class Booking System

A Django-based CRUD web application for managing and booking gym classes. Built as part of the IS424 Web Application Development course at King Saud University.

---

## Features

- User registration and login
- Browse all available gym classes
- View class details and book/cancel a spot
- Personal bookings dashboard
- Admin-only: add and update classes
- Responsive orange & white UI built with Bootstrap 5

## Tech Stack

- **Backend:** Django 5 (Python)
- **Database:** SQLite
- **Frontend:** Bootstrap 5, Bootstrap Icons, Google Fonts (Inter)

## Project Structure

```
├── gym_core/          # Django project settings and root URLs
├── gym_app/           # Main application
│   ├── models.py      # GymClass and Booking models
│   ├── views.py       # All views
│   ├── forms.py       # Login, registration, and class forms
│   ├── urls.py        # App URL patterns
│   └── templates/     # HTML templates
├── seed_data.py       # Sample data script
├── report.html        # Project report (print to PDF)
├── requirements.txt
└── manage.py
```

## Setup & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Seed sample data
Get-Content seed_data.py | python manage.py shell

# Start the development server
python manage.py runserver
```

Then open **http://127.0.0.1:8000/** in your browser.

## Demo Accounts

| Username | Password | Role  |
|----------|----------|-------|
| `admin`  | `admin123` | Admin (can add/edit classes) |
| `khalid` | `pass1234` | Member |
| `faisal` | `pass1234` | Member |

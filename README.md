# Waste Management

A community waste-reporting web app built with Django. Residents can submit reports about waste issues, include a location and optional photo, and browse report details and their current status.

## Live demo

[Open the Waste Management app](https://waste-management-hc22.onrender.com/waste/)

## Features

- Browse community waste reports, newest first.
- Submit a report with a title, location, description, reporter name, optional phone number, and optional photo.
- View an individual report, including its status (`Pending`, `In Progress`, or `Cleaned`).
- Manage reports in the Django admin, with status filtering and search by location or title.

## Tech stack

- Python and Django 5.0.6
- SQLite for the default database
- Gunicorn and WhiteNoise for deployment and static-file serving

## Run locally

Requires Python 3. Install dependencies, apply database migrations, and start the Django development server:

```bash
git clone https://github.com/borah12/waste_management.git
cd waste_management
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/waste/>. The project uses SQLite by default, stored in `db.sqlite3`.

## Main routes

- `/waste/` — community report list
- `/waste/waste/` — submit a waste report
- `/waste/waste/<id>/` — report details
- `/admin/` — Django administration

## Project layout

```text
waste/                  Report model, form, views, routes, admin, and templates
waste/templates/waste/  Report list, creation, and detail pages
waste/migrations/       Database schema migrations
waste_management/       Django project settings and root URL configuration
reports/                Uploaded report images
manage.py               Django command-line entry point
requirements.txt        Python dependencies
build.sh                Deployment build steps (install, collect static files, migrate)
Procfile                Web process declaration
```

## Deployment

The repository includes a `build.sh` script that installs dependencies, collects static files, and runs migrations. The `Procfile` declares the web process. For production deployments, configure a secure Django `SECRET_KEY`, turn off `DEBUG`, and set appropriate `ALLOWED_HOSTS` values rather than using the development settings as-is.

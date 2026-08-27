# Internee.pk Backend

Django backend for the Internee.pk internship platform. Handles user authentication, task tracking, and submission management.

## Tech Stack
- Django 6.0.6
- Django REST Framework
- SQLite (dev) — PostgreSQL-ready for production
- python-dotenv for environment config

## Features (Task 2)
- Custom User model with role-based field (`admin`, `staff`, `user`) — foundation for future RBAC
- Task and Submission models with relational tracking
- Session-based authentication (login/logout)
- Explore page: browse tasks, submit progress
- Dashboard page: view your submission status
- Query optimization via `select_related` to avoid N+1 queries
- Security: HTTPOnly cookies, CSRF protection, clickjacking protection, HTTPS-ready settings
- Automated tests covering auth flow and submission creation



## Features (Task 3)

- Full REST API (CRUD) for Tasks and Submissions via Django REST Framework
- Custom permission system — read access for all authenticated users, write access (create/update/delete) restricted to `admin`/`staff` roles
- DRF ViewSets + Router for automatic URL generation (`/api/tasks/`, `/api/submissions/`)
- Basic Authentication support for API testing (Postman-verified)
- Automated tests covering role-based API permissions (staff can create, regular users blocked)



## Setup


pip install -r requirements.txt


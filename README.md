# Internee.pk Backend

Django backend suite for the Internee.pk internship platform, covering backend development, REST API, database optimization, deployment, and role-based access control.





> **Task 2 — Document Management System with AI Search** is a separate, standalone project. See its dedicated repo: [document-management-system](#) https://github.com/HaseebAhmed033/document-management-system


-Due to time constraint this task was not fully accomplished



## Tech Stack
- Django 6.0.6
- Django REST Framework
- SQLite (dev) — PostgreSQL-ready for production (Neon/Railway compatible)
- python-dotenv for environment config
- Gunicorn + Whitenoise (production server + static files)
- Django Debug Toolbar (query profiling)




## Task 3 — Django Backend Development for Internee.pk
- Custom User model with role-based field (`admin`, `staff`, `user`)
- Task and Submission models with relational tracking
- Session-based authentication (login/logout)
- Explore page: browse tasks, submit progress
- Dashboard page: view your submission status
- Query optimization via `select_related` to avoid N+1 queries
- Security: HTTPOnly cookies, CSRF protection, clickjacking protection, HTTPS-ready settings
- Automated tests covering auth flow and submission creation





## Task 4 — REST API
- Full REST API (CRUD) for Tasks and Submissions via Django REST Framework
- Custom permission system — read access for all authenticated users, write access (create/update/delete) restricted to `admin`/`staff` roles
- DRF ViewSets + Router for automatic URL generation (`/api/tasks/`, `/api/submissions/`)
- Basic Authentication support for API testing (Postman-verified)
- Automated tests covering role-based API permissions (staff can create, regular users blocked)





## Task 5 — Database Optimization & Performance Tuning
- DB indexes added on frequently-queried fields (`Task.created_at`, `Submission.status`, composite `Submission.user + status`)
- `select_related` applied on Submission querysets to eliminate N+1 queries
- Django local-memory caching applied to task list API endpoint (`@cache_page`)
- Django Debug Toolbar integrated for live query count/time profiling — verified working, screenshot available on request





## Task 6 — Deployment & Scalability
- Deployed to Railway: https://web-production-7ee8f.up.railway.app/
- Build and deploy succeeded; app is live on Railway's infrastructure
- **Known issue:** production PostgreSQL database migration was not completed before the submission deadline — Railway's Postgres instance did not have public network access enabled in time to run `migrate` from a local machine, and the live URL may not be fully functional as a result
- Core application logic, models, API, permissions, and optimizations are fully built, tested, and verified working in the local development environment (SQLite)
- Load balancing / horizontal scaling and Redis caching were scoped out due to time constraints; Django's built-in local-memory cache was used instead as a documented, lighter-weight substitute




## Task 7 — User Authentication & Role-Based Access Control
- Custom `role` field (`admin`/`staff`/`user`) on the User model, established in Task 3
- Custom DRF permission class (`IsAdminOrStaffOrReadOnly`) enforcing:
  - Any authenticated user → read access (GET)
  - Only `admin`/`staff` roles → write access (POST/PUT/DELETE)
- Applied consistently across Task and Submission API endpoints




## Setup

pip install -r requirements.txt


Create a `.env` file with:

SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3







## Known Limitations / Future Improvements
- Production database migration verification (blocked by Railway public networking setup under time pressure)
- Redis-based caching instead of local-memory cache
- CI/CD pipeline for automated deployment
- Load balancing and horizontal scaling configuration
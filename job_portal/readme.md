Job Portal Backend
A basic job portal backend built with Django and Django REST Framework (DRF), supporting user roles, job postings, and job applications.
Setup Instructions

Create a Virtual Environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:pip install -r requirements.txt

Run Migrations:python manage.py makemigrations
python manage.py migrate

Create a Superuser (optional, for admin access):python manage.py createsuperuser

Run the Server:python manage.py runserver

The API will be available at http://localhost:8000/api/.
API Endpoints
Authentication

- Register: POST /api/users/register/
- Request: { "username": "string", "email": "string", "password": "string", "role": "seeker|employer" }
- Response: { "token": "string", "user": { "id": int, "username": "string", "email": "string", "role": "string" } }

- Login: POST /api/users/login/
- Request: { "username": "string", "password": "string" }
- Response: { "token": "string", "user": { "id": int, "username": "string", "email": "string", "role": "string" } }

Jobs (Authenticated for Employers, Public for Listing)

List/Create Jobs: GET/POST /api/jobs/  

- GET: List all active jobs (public) or employer’s jobs (if employer).
- Filters: ?location=string&job_type=string&search=keyword  

POST: Create a job (employers only).
- Request: { "title": "string", "description": "string", "location": "string", "salary_range": "string", "job_type": "full_time|part_time|contract|internship" }


Retrieve/Update/Delete Job: GET/PUT/DELETE /api/jobs/<id>/ (employers only for PUT/DELETE)

Applications (Authenticated for Job Seekers)

List/Create Applications: GET/POST /api/applications/  
GET: List seeker’s applications.  
POST: Apply to a job.Request: { "job": int, "cover_letter": "string" }


Retrieve Application: GET /api/applications/<id>/

Authentication

Use Authorization: Token <token> header for authenticated requests.

Notes

SQLite is used as the database for simplicity.
Employers can only manage their own job postings.
Job Seekers can only apply once per job.
Use Django admin (/admin/) for manual data management.


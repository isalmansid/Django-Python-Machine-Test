# Django Python Machine Test



1. Install latest version of Python

2. MySQL: Download and Install MySQL.

3. Create a new directory for the project and navigate to it:

```bash
mkdir Django-Python-Machine-Test
cd Django-Python-Machine-Test
```

4. Install Django and other dependencies:

```bash
pip install django djangorestframework psycopg2-binary
```

5. Start a new Django project:

```bash
django-admin startproject machine_test
cd machine_test
```

6. Create a new Django app:

```bash
python manage.py startapp core
```

7. Register the app (core) in INSTALLED_APPS in the settings.py file:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'core',
]




# Running the Code

```bash
pip install -r requirements.txt
```


1. In the settings.py file, configure the database to use PostgreSQL or MySQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use 'django.db.backends.postgresql' for postgresql
        'NAME': 'machine_test',  # Replace with your DB name
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',  # Or the database server IP
        'PORT': '3306',  # 5432 for postgresql
    }
}


2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```


3. Create a superuser for the admin panel:

```bash
python manage.py createsuperuser
```


4. Start the Development Server

```bash
python manage.py runserver
```

5. Visit http://127.0.0.1:8000/admin to access the admin panel and log in using the superuser credentials.




# Machine Test using Postman and seed the database

1. Use Postman to test the API endpoints:

List/Create Clients:

GET /api/clients/ → Lists all clients.
POST /api/clients/ → Creates a new client. 

{
    "client_name": "Test Client"
}



- Retrieve/Update/Delete a Client:

GET /api/clients/<id>/ → Retrieves details of a client.
PUT/PATCH /api/clients/<id>/ → Updates client details.
DELETE /api/clients/<id>/ → Deletes a client.

List/Create Projects:

GET /api/projects/ → Lists all projects.
POST /api/projects/ → Creates a new project.
{
    "project_name": "Test Project",
    "client_id": 1,
    "users": [1, 2]
}


- List Projects Assigned to a User:

GET /api/projects/assigned/ → Lists all projects assigned to the logged-in user.
Delete a Project:

DELETE /api/projects/<id>/ → Deletes a project.


2. Test User Authentication:

Ensure that the Authorization header is set with a valid token (JWT or session-based).

access token /api/token/ → get access token

{
    "username": "name",
    "password": "password"
}






# DB Design




+--------------------+       +--------------------+       +--------------------+
|       User         |       |       Client       |       |      Project       |
+--------------------+       +--------------------+       +--------------------+
| id (PK)           |       | id (PK)           |       | id (PK)           |
| username          |       | client_name       |       | project_name      |
| email             |       | created_by (FK)   |<------| client_id (FK)    |
| password          |       | created_at        |       | created_by (FK)   |
+--------------------+       | updated_at        |       | created_at        |
                             +--------------------+       | updated_at        |
                                                         +--------------------+
                                                               |
                                                               |
                                                       +--------------------+
                                                       | User_Project (M2M) |
                                                       +--------------------+
                                                       | id (PK)           |
                                                       | user_id (FK)      |
                                                       | project_id (FK)   |
                                                       +--------------------+







- Models
User: Represents a user in the system.
Client: Represents a client in the system. Linked to a user via the created_by field.
Project: Represents a project, linked to:
A Client via the client_id field.
Multiple Users via a many-to-many relationship (User_Project).



























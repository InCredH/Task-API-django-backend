Django Task Management API
This Django project serves as a Task Management API allowing users to create, update, retrieve, and delete tasks. It offers the following features:

Features
Token-Based Authentication: Users can authenticate via tokens to access protected API endpoints.
CRUD Operations: Supports Create, Read, Update, and Delete operations for tasks.
Permission Control: Users can only modify or delete tasks they own.

Getting Started
Installation
Clone this repository:
git clone https://github.com/InCredH/django-task-management.git
pipenv install
cd taskrestapi

Create Superuser:
python manage.py createsuperuser

Apply database migrations:
python manage.py migrate

Running the Server
Start the development server:
python manage.py runserver
The server will start at http://127.0.0.1:8000/.

API Endpoints
Tasks
GET /api/tasks/: Retrieve all tasks.
POST /api/tasks/: Create a new task.
GET /api/tasks/<task_id>/: Retrieve a specific task.
PUT /api/tasks/<task_id>/: Update a specific task.
DELETE /api/tasks/<task_id>/: Delete a specific task.

Authentication
POST /api/token/: Obtain a token for authentication.
POST /api/token/refresh/: Refresh a token (if valid).

You can use a GUI client like Postman. Here I am showing it in CLI.

Usage
Authentication:
Use the /api/token/ endpoint to obtain an access token by providing valid credentials. Include the token in the Authorization header for authenticated requests.

Example:
curl -X POST -H "Content-Type: application/json" -d '{"username": "your_username", "password": "your_password"}' http://127.0.0.1:8000/api/token/

API Endpoints:
Utilize the provided API endpoints to manage tasks. Ensure authentication headers are included for protected endpoints.

Example:
curl -H "Authorization: Bearer <your_access_token>" http://127.0.0.1:8000/api/tasks/
Contributing
Feel free to contribute to this project by forking the repository and submitting pull requests with your enhancements.

License
This project is licensed under the MIT License - see the LICENSE file for details.
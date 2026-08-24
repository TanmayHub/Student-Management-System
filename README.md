Student Management System

A backend REST API for managing student records, built using Python, FastAPI, SQLAlchemy, MySQL, and JWT-based authentication.

The system provides secure APIs for creating, reading, updating, and deleting student records. Authentication and authorization are implemented to ensure that only authorized users can access protected operations.

🚀 Features
Create student records
Retrieve student records
Retrieve a student by ID
Update student information
Delete student records
JWT-based user authentication
Role-based authorization
Protected API endpoints
Request validation using Pydantic
Database integration using SQLAlchemy ORM
MySQL database support
Dependency Injection using FastAPI
Proper HTTP status codes and error handling
Logging for important application events
Interactive API documentation using Swagger UI
🛠️ Technologies Used
Technology	Purpose
Python	Backend programming language
FastAPI	REST API framework
SQLAlchemy	ORM and database interaction
MySQL	Relational database
PyMySQL	MySQL database driver
Pydantic	Request/response validation
JWT	Authentication
Uvicorn	ASGI server
Git & GitHub	Version control

🏗️ Project Architecture

The project follows a layered backend structure:

Client
   │
   ▼
FastAPI Router
   │
   ▼
Authentication / Authorization
   │
   ▼
Schema Validation
   │
   ▼
CRUD / Service Logic
   │
   ▼
SQLAlchemy ORM
   │
   ▼
MySQL Database
Request Flow
HTTP Request
     ↓
FastAPI Endpoint
     ↓
JWT Authentication
     ↓
Authorization Check
     ↓
Pydantic Validation
     ↓
CRUD Function
     ↓
SQLAlchemy
     ↓
MySQL
     ↓
HTTP Response
📁 Project Structure
student-management-system/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   │
│   ├── auth.py
│   ├── dependencies.py
│   │
│   └── routers/
│       ├── __init__.py
│       ├── students.py
│       └── auth.py
│
├── tests/
│   └── ...
│
├── requirements.txt
├── .gitignore
└── README.md

The exact folder names may differ depending on the final structure of the repository.

🔐 Authentication & Authorization

The application uses JWT (JSON Web Token) authentication.

The basic authentication flow is:

User Login
    ↓
Credentials Verified
    ↓
JWT Token Generated
    ↓
Client Sends Token
    ↓
FastAPI Validates Token
    ↓
User Identity / Role Extracted
    ↓
Authorization Check
    ↓
Protected Endpoint Access
Authentication

Authentication answers:

"Who are you?"

The user provides valid credentials and receives a JWT access token.

Authorization

Authorization answers:

"What are you allowed to do?"

After authentication, the user's role/permissions are checked before allowing access to protected operations.

🗄️ Database

The application uses MySQL as the relational database.

SQLAlchemy is used as the ORM layer so that the application can interact with database tables using Python objects instead of writing raw SQL for every operation.

Example Student Entity

A student record can contain information such as:

id
name
email
age
course

The exact fields depend on the implementation of the project.

📡 API Endpoints
Authentication
Login
POST /login

Used to authenticate a user and generate a JWT access token.

Students
Create Student
POST /students/

Creates a new student record.

Requires:

Authentication
Appropriate authorization

Example request:

{
  "name": "Rahul Sharma",
  "email": "rahul@example.com",
  "age": 21,
  "course": "Computer Science"
}
Get All Students
GET /students/

Returns a list of students.

Get Student by ID
GET /students/{student_id}

Returns a specific student based on their ID.

Example:

GET /students/1
Update Student
PUT /students/{student_id}

Updates an existing student's information.

Example:

{
  "name": "Rahul Sharma",
  "email": "rahul.new@example.com",
  "age": 22,
  "course": "Information Technology"
}
Delete Student
DELETE /students/{student_id}

Deletes a student record.

✅ Validation

Pydantic schemas are used to validate incoming request data before it reaches the database.

For example, invalid or incomplete data can result in an appropriate validation error instead of inserting incorrect information into the database.

FastAPI automatically returns validation errors with appropriate HTTP responses.

🔒 Protected Endpoints

Protected endpoints require a valid JWT access token.

Requests without a valid token can be rejected with an appropriate authentication error.

Authorization is additionally used to prevent users from performing operations for which they do not have permission.

💉 Dependency Injection

FastAPI's dependency injection system is used for reusable application components such as:

Database sessions
Current authenticated user
Authentication checks
Authorization checks

For example, a database session can be injected into an endpoint instead of manually creating a new database connection inside every route.

This improves:

Code reusability
Maintainability
Testability
Separation of responsibilities

⚙️ Installation & Setup

1. Clone the Repository
git clone <your-github-repository-url>

Move into the project directory:

cd student-management-system
2. Create a Virtual Environment
python -m venv venv

Activate it on Windows:

venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure MySQL

Create a MySQL database for the application.

Example:

CREATE DATABASE student_management;

Configure the database connection in the application's database configuration.

Example:

mysql+pymysql://username:password@localhost/student_management

Do not commit real database passwords or secret keys to GitHub.

🔑 Environment Variables

Sensitive configuration such as database credentials and JWT secrets should ideally be stored in environment variables.

Example:

DATABASE_URL=mysql+pymysql://username:password@localhost/student_management
SECRET_KEY=your-secret-key
ALGORITHM=HS256

Add your environment file to .gitignore:

.env
venv/
__pycache__/
▶️ Running the Application

Start the FastAPI application using Uvicorn:

uvicorn app.main:app --reload

The API will normally be available at:

http://127.0.0.1:8000
📚 API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI

Open:

http://127.0.0.1:8000/docs

Swagger UI allows you to:

View available endpoints
See request schemas
Send API requests
Test authentication
Test protected endpoints
Inspect API responses
ReDoc

Alternative documentation is available at:

http://127.0.0.1:8000/redoc
🧪 Testing the API

The API can be tested using Swagger UI, Postman, or another API client.

Recommended testing flow:

1. Start the application
       ↓
2. Authenticate / Login
       ↓
3. Obtain JWT access token
       ↓
4. Authorize the API client
       ↓
5. Create a student
       ↓
6. Get all students
       ↓
7. Get student by ID
       ↓
8. Update student
       ↓
9. Delete student
       ↓
10. Test unauthorized requests
       ↓
11. Test invalid student IDs
       ↓
12. Test invalid request data
🧪 Example Test Cases
Test Case	Expected Result
Valid login credentials	JWT token generated
Invalid login credentials	Authentication failure
Create student with valid data	Student created
Create student without authentication	Request rejected
Get all students	Student list returned
Get existing student	Student returned
Get non-existing student	Appropriate error returned
Update existing student	Student updated
Delete existing student	Student deleted
Invalid request body	Validation error
Invalid JWT token	Authentication failure
Unauthorized role	Authorization failure
📌 HTTP Status Codes

The API uses standard HTTP status codes to communicate the result of requests.

Common responses include:

200 OK
201 Created
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
422 Unprocessable Entity
500 Internal Server Error
🧠 Key Backend Concepts Demonstrated

This project demonstrates practical understanding of:

REST API development
FastAPI
HTTP methods
CRUD operations
SQLAlchemy ORM
MySQL
Pydantic validation
JWT authentication
Authorization
Dependency Injection
Database sessions
API documentation
Error handling
Logging
Virtual environments
Python package management
Git and GitHub
🔄 CRUD Operations

The core student management functionality follows CRUD:

C → Create
R → Read
U → Update
D → Delete

Example:

POST   → Create Student
GET    → Read Students
PUT    → Update Student
DELETE → Delete Student
🔐 Security Considerations

The project follows several basic backend security practices:

JWT-based authentication
Authorization for protected operations
Passwords should not be stored as plain text
Secret keys should be stored outside source code
Environment variables should be used for sensitive configuration
.env files should not be committed to GitHub
Input data is validated before processing
📦 Requirements

The main dependencies are listed in requirements.txt.

Example:

fastapi
uvicorn
sqlalchemy
pymysql
pydantic

Additional packages may be included depending on the authentication and logging implementation.

Install everything using:

pip install -r requirements.txt
🎯 Project Objective

The main objective of this project is to build a secure and structured backend REST API for student management while applying real-world backend development concepts.

The project focuses on:

Building APIs with FastAPI
Connecting APIs to MySQL
Managing data using SQLAlchemy
Validating API requests
Implementing authentication
Implementing authorization
Handling database operations
Structuring a maintainable backend application
🚀 Future Improvements

Possible future improvements include:

Password hashing using bcrypt/Argon2
Refresh token support
Pagination for student records
Search and filtering
Sorting
Advanced role-based permissions
Automated unit and integration tests
Docker support
CI/CD using GitHub Actions
Production deployment
API rate limiting
Centralized exception handling

👨‍💻 Author

Tanmaya Kumar Yadav


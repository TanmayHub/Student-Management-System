# 🎓 Student Management System

A backend REST API for managing student records, built using **Python, FastAPI, SQLAlchemy, MySQL, and JWT-based Authentication & Authorization**.

The system provides secure APIs for creating, reading, updating, and deleting student records while protecting sensitive operations through authentication and authorization.

---

## 🚀 Features

* ✅ Create student records
* ✅ Retrieve all students
* ✅ Retrieve a student by ID
* ✅ Update student information
* ✅ Delete student records
* ✅ JWT-based authentication
* ✅ Role-based authorization
* ✅ Protected API endpoints
* ✅ Request validation using Pydantic
* ✅ MySQL database integration
* ✅ SQLAlchemy ORM
* ✅ FastAPI Dependency Injection
* ✅ Proper HTTP status codes
* ✅ Error handling
* ✅ Application logging
* ✅ Interactive Swagger API documentation

---

## 🛠️ Technologies Used

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| **Python**       | Backend programming language    |
| **FastAPI**      | REST API framework              |
| **SQLAlchemy**   | ORM and database interaction    |
| **MySQL**        | Relational database             |
| **PyMySQL**      | MySQL database driver           |
| **Pydantic**     | Request and response validation |
| **JWT**          | Authentication                  |
| **Uvicorn**      | ASGI server                     |
| **Git & GitHub** | Version control                 |

---

## 🏗️ Project Architecture

The application follows a layered backend architecture:

```text
Client
   │
   ▼
FastAPI Router
   │
   ▼
Authentication & Authorization
   │
   ▼
Pydantic Schema Validation
   │
   ▼
CRUD / Business Logic
   │
   ▼
SQLAlchemy ORM
   │
   ▼
MySQL Database
```

### Request Flow

```text
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
```

---

## 📁 Project Structure

```text
student-management-system/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
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
```

> Update the structure above if your actual project folders/files are different.

---

# 🔐 Authentication & Authorization

The application uses **JWT (JSON Web Token)** for authentication.

### Authentication Flow

```text
User Login
    ↓
Credentials Verified
    ↓
JWT Access Token Generated
    ↓
Client Sends Token
    ↓
FastAPI Validates Token
    ↓
User Identity Extracted
    ↓
Authorization Check
    ↓
Protected Endpoint Access
```

### Authentication

Authentication answers:

> **"Who are you?"**

A user provides valid credentials and receives a JWT access token.

### Authorization

Authorization answers:

> **"What are you allowed to do?"**

After authentication, the user's role or permissions are checked before allowing access to protected operations.

---

# 🗄️ Database

The application uses **MySQL** as the relational database.

**SQLAlchemy** is used as the ORM layer to communicate with the database using Python objects and models.

### Example Student Entity

A student record can contain information such as:

```text
id
name
email
age
course
```

The exact fields depend on the implementation of the project.

---

# 📡 API Endpoints

## 🔑 Authentication

### Login

```http
POST /login
```

Authenticates a user and generates a JWT access token.

---

## 👨‍🎓 Student APIs

### Create Student

```http
POST /students/
```

Creates a new student record.

**Authentication:** Required

**Authorization:** Required

Example request:

```json
{
  "name": "Rahul Sharma",
  "email": "rahul@example.com",
  "age": 21,
  "course": "Computer Science"
}
```

---

### Get All Students

```http
GET /students/
```

Returns a list of all students.

---

### Get Student by ID

```http
GET /students/{student_id}
```

Returns a specific student based on the student ID.

Example:

```http
GET /students/1
```

---

### Update Student

```http
PUT /students/{student_id}
```

Updates an existing student's information.

Example:

```json
{
  "name": "Rahul Sharma",
  "email": "rahul.new@example.com",
  "age": 22,
  "course": "Information Technology"
}
```

---

### Delete Student

```http
DELETE /students/{student_id}
```

Deletes a student record from the database.

---

# ✅ Data Validation

**Pydantic schemas** are used to validate incoming request data before it reaches the database.

For example:

* Required fields are validated
* Data types are validated
* Invalid request bodies are rejected
* Incorrect input generates validation errors

FastAPI automatically returns appropriate validation responses.

---

# 🔒 Protected Endpoints

Protected endpoints require a valid JWT access token.

If a request does not contain a valid token, the API rejects the request.

Authorization is also used to prevent authenticated users from performing operations for which they do not have permission.

---

# 💉 Dependency Injection

FastAPI's **Dependency Injection** system is used for reusable application components such as:

* Database sessions
* Current authenticated user
* Authentication checks
* Authorization checks

For example, a database session can be injected into an endpoint rather than creating a new database connection manually inside every route.

This improves:

* Code reusability
* Maintainability
* Testability
* Separation of responsibilities

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd student-management-system
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure MySQL

Create a MySQL database for the application.

Example:

```sql
CREATE DATABASE student_management;
```

Configure your database connection in the application.

Example:

```text
mysql+pymysql://username:password@localhost/student_management
```

> ⚠️ Never commit real database passwords or secret keys to GitHub.

---

# 🔑 Environment Variables

Sensitive configuration such as database credentials and JWT secrets should be stored using environment variables.

Example:

```env
DATABASE_URL=mysql+pymysql://username:password@localhost/student_management
SECRET_KEY=your-secret-key
ALGORITHM=HS256
```

Add sensitive files and folders to `.gitignore`:

```text
.env
venv/
__pycache__/
```

---

# ▶️ Running the Application

Start the FastAPI application using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

---

# 📚 API Documentation

FastAPI automatically generates interactive API documentation.

## Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to:

* View available endpoints
* View request schemas
* Send API requests
* Test authentication
* Test protected endpoints
* Inspect API responses

## ReDoc

Alternative API documentation:

```text
http://127.0.0.1:8000/redoc
```

---

# 🧪 Testing the API

The API can be tested using:

* Swagger UI
* Postman
* Any REST API client

### Recommended Testing Flow

```text
1. Start the application
        ↓
2. Login
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
```

---

# 🧪 Example Test Cases

| Test Case                             | Expected Result            |
| ------------------------------------- | -------------------------- |
| Valid login credentials               | JWT token generated        |
| Invalid login credentials             | Authentication failure     |
| Create student with valid data        | Student created            |
| Create student without authentication | Request rejected           |
| Get all students                      | Student list returned      |
| Get existing student                  | Student returned           |
| Get non-existing student              | Appropriate error returned |
| Update existing student               | Student updated            |
| Delete existing student               | Student deleted            |
| Invalid request body                  | Validation error           |
| Invalid JWT token                     | Authentication failure     |
| Unauthorized role                     | Authorization failure      |

---

# 📌 HTTP Status Codes

The API uses standard HTTP status codes.

| Status Code | Meaning               |
| ----------- | --------------------- |
| **200**     | OK                    |
| **201**     | Created               |
| **204**     | No Content            |
| **400**     | Bad Request           |
| **401**     | Unauthorized          |
| **403**     | Forbidden             |
| **404**     | Not Found             |
| **422**     | Validation Error      |
| **500**     | Internal Server Error |

---

# 🔄 CRUD Operations

The core student management functionality follows **CRUD**:

```text
C → Create
R → Read
U → Update
D → Delete
```

| HTTP Method | Operation      |
| ----------- | -------------- |
| **POST**    | Create Student |
| **GET**     | Read Students  |
| **PUT**     | Update Student |
| **DELETE**  | Delete Student |

---

# 🧠 Backend Concepts Demonstrated

This project demonstrates practical understanding of:

* REST API development
* FastAPI
* HTTP methods
* CRUD operations
* SQLAlchemy ORM
* MySQL
* Pydantic validation
* JWT authentication
* Authorization
* Dependency Injection
* Database sessions
* API documentation
* Error handling
* Logging
* Virtual environments
* Python package management
* Git and GitHub

---

# 🔐 Security Considerations

The project follows basic backend security practices:

* JWT-based authentication
* Authorization for protected operations
* Passwords should not be stored as plain text
* Secret keys should not be hardcoded
* Sensitive configuration should use environment variables
* `.env` files should not be committed to GitHub
* Input data should be validated before processing

---

# 📦 Requirements

The main dependencies are listed in `requirements.txt`.

Example:

```text
fastapi
uvicorn
sqlalchemy
pymysql
pydantic
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 🎯 Project Objective

The main objective of this project is to build a **secure and structured backend REST API for student management** while applying real-world backend development concepts.

The project focuses on:

* Building REST APIs using FastAPI
* Connecting APIs to MySQL
* Managing database operations using SQLAlchemy
* Validating API requests using Pydantic
* Implementing JWT authentication
* Implementing authorization
* Handling CRUD operations
* Using dependency injection
* Structuring a maintainable backend application

---

# 🚀 Future Improvements

Possible future improvements include:

* Password hashing using bcrypt or Argon2
* Refresh token support
* Pagination
* Student search and filtering
* Sorting
* Advanced role-based permissions
* Automated unit tests
* Integration testing
* Docker support
* CI/CD using GitHub Actions
* Production deployment
* API rate limiting
* Centralized exception handling

---

# 👨‍💻 Author

**Tanmaya Kumar Yadav**

Python Backend Developer | FastAPI | SQL | REST APIshe repository a ⭐ on GitHub.

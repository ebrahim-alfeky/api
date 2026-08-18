# 🎬 Django REST API - Movie Reservation System

---

## 📌 Overview

A comprehensive **Django REST API** project that demonstrates **multiple approaches** to building RESTful APIs, including **Function-Based Views**, **APIView classes**, **Mixins**, **Generic Views**, and **ViewSets**. The application features a **movie reservation system** with complete CRUD operations, **three authentication mechanisms** (Session, Token, JWT), pagination, and webhook integration.

---

## ✨ Key Features

### 🎭 Core Features

* **Movie Management** - Create, read, update, delete movies
* **Guest Management** - Manage guest information
* **Reservation System** - Book movie reservations with guests
* **Multiple API Styles** - Demonstrates 5 different API implementation approaches
* **Pagination** - Built-in page-based pagination (5 items per page)

### 🔐 Authentication Systems (3 Types)

1. **Session Authentication** - Traditional Django session-based
2. **Token Authentication** - DRF Token-based authentication
3. **JWT Authentication** - JSON Web Token with refresh/access tokens

### 🛠️ API Implementation Patterns

1. **Function-Based Views** - Simple `@api_view` decorator
2. **APIView Classes** - Class-based views with full control
3. **Mixins + GenericAPIView** - Reusable CRUD components
4. **Generic Views** - `ListCreateAPIView` & `RetrieveUpdateDestroyAPIView`
5. **ViewSets** - `ModelViewSet` for automatic routing

### 🔄 Additional Features

* **Custom Find Movie** - Search by movie name and hall
* **Custom Reservation** - Create reservations with guest creation
* **Cookie Management** - Set and retrieve HTTP-only cookies
* **GitHub Webhook** - Endpoint for receiving GitHub webhook payloads
* **CSRF Exemption** - For webhook endpoints

---

## 🛠️ Technology Stack

| Category              | Technology                      |
| --------------------- | ------------------------------- |
| **Backend Framework** | Django 5.1.5                    |
| **API Framework**     | Django REST Framework 3.16.0    |
| **Authentication**    | Session, Token, JWT (SimpleJWT) |
| **Database**          | SQLite (default)                |
| **Token Management**  | DRF Authtoken, SimpleJWT        |
| **Environment**       | Python 3.8+                     |

---

## 📁 Project Structure

```text
ebrahim-alfeky-api/
├── manage.py
├── requirements.txt
├── README.md
├── app1/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializer.py
│   ├── views.py
│   ├── tests.py
│   └── migrations/
│       ├── 0001_initial.py
│       ├── 0002_delete_testmodel_remove_reservation_guests_and_more.py
│       └── __init__.py
└── project/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## 🚀 Installation & Setup

### 1. Clone & Navigate

```bash
git clone <repository-url>
cd ebrahim-alfeky-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

### 7. Access the Application

* **API Root:** `http://localhost:8000/`
* **Admin Panel:** `http://localhost:8000/admin/`

---

## 📡 API Endpoints

### 🎬 Movie Endpoints

| Method     | Endpoint               | Description                 | Implementation |
| ---------- | ---------------------- | --------------------------- | -------------- |
| **GET**    | `/movie/`              | List all movies (paginated) | APIView        |
| **POST**   | `/movie/`              | Create new movie            | APIView        |
| **GET**    | `/movie/<id>/`         | Get movie details           | APIView        |
| **PATCH**  | `/movie/<id>/`         | Update movie                | APIView        |
| **DELETE** | `/movie/<id>/`         | Delete movie                | APIView        |
| **GET**    | `/movie_mixin/`        | List all movies             | Mixins         |
| **POST**   | `/movie_mixin/`        | Create new movie            | Mixins         |
| **GET**    | `/movie_mixin/<pk>/`   | Get movie details           | Mixins         |
| **PUT**    | `/movie_mixin/<pk>/`   | Update movie                | Mixins         |
| **DELETE** | `/movie_mixin/<pk>/`   | Delete movie                | Mixins         |
| **GET**    | `/movie_generic/`      | List all movies             | Generic Views  |
| **POST**   | `/movie_generic/`      | Create new movie            | Generic Views  |
| **GET**    | `/movie_generic/<pk>/` | Get movie details           | Generic Views  |
| **PUT**    | `/movie_generic/<pk>/` | Update movie                | Generic Views  |
| **DELETE** | `/movie_generic/<pk>/` | Delete movie                | Generic Views  |
| **GET**    | `/movie_viewset/`      | List all movies             | ViewSet        |
| **POST**   | `/movie_viewset/`      | Create new movie            | ViewSet        |
| **GET**    | `/movie_viewset/<pk>/` | Get movie details           | ViewSet        |
| **PUT**    | `/movie_viewset/<pk>/` | Update movie                | ViewSet        |
| **DELETE** | `/movie_viewset/<pk>/` | Delete movie                | ViewSet        |

### 👤 Guest Endpoints

| Method     | Endpoint               | Description       | Implementation |
| ---------- | ---------------------- | ----------------- | -------------- |
| **GET**    | `/guest/`              | List all guests   | APIView        |
| **POST**   | `/guest/`              | Create new guest  | APIView        |
| **PUT**    | `/guest/<id>/`         | Update guest      | APIView        |
| **DELETE** | `/guest/<id>/`         | Delete guest      | APIView        |
| **GET**    | `/guest_mixin/`        | List all guests   | Mixins         |
| **POST**   | `/guest_mixin/`        | Create new guest  | Mixins         |
| **GET**    | `/guest_mixin/<pk>/`   | Get guest details | Mixins         |
| **PUT**    | `/guest_mixin/<pk>/`   | Update guest      | Mixins         |
| **DELETE** | `/guest_mixin/<pk>/`   | Delete guest      | Mixins         |
| **GET**    | `/guest_generic/`      | List all guests   | Generic Views  |
| **POST**   | `/guest_generic/`      | Create new guest  | Generic Views  |
| **GET**    | `/guest_generic/<pk>/` | Get guest details | Generic Views  |
| **PUT**    | `/guest_generic/<pk>/` | Update guest      | Generic Views  |
| **DELETE** | `/guest_generic/<pk>/` | Delete guest      | Generic Views  |
| **GET**    | `/guest_viewset/`      | List all guests   | ViewSet        |
| **POST**   | `/guest_viewset/`      | Create new guest  | ViewSet        |

### 🎟️ Reservation Endpoints

| Method     | Endpoint                | Description            | Implementation |
| ---------- | ----------------------- | ---------------------- | -------------- |
| **GET**    | `/reversation/`         | List all reservations  | APIView        |
| **POST**   | `/reversation/`         | Create new reservation | APIView        |
| **PUT**    | `/reversation/<id>/`    | Update reservation     | APIView        |
| **DELETE** | `/reversation/<id>/`    | Delete reservation     | APIView        |
| **GET**    | `/reversation_mixin/`   | List all reservations  | Mixins         |
| **POST**   | `/reversation_mixin/`   | Create new reservation | Mixins         |
| **GET**    | `/reversation_generic/` | List all reservations  | Generic Views  |
| **POST**   | `/reversation_generic/` | Create new reservation | Generic Views  |
| **GET**    | `/reservation_viewset/` | List all reservations  | ViewSet        |

### 🔐 Authentication Endpoints

#### Session Authentication

| Method   | Endpoint   | Description             |
| -------- | ---------- | ----------------------- |
| **POST** | `/signup/` | Create new user         |
| **POST** | `/login/`  | Login with session      |
| **POST** | `/logout/` | Logout (clears cookies) |

#### Token Authentication

| Method   | Endpoint                  | Description     |
| -------- | ------------------------- | --------------- |
| **POST** | `/token/signup/`          | Create new user |
| **POST** | `/token/login/`           | Get auth token  |
| **POST** | `/token/logout/`          | Delete token    |
| **POST** | `/token/change_password/` | Change password |

#### JWT Authentication

| Method   | Endpoint                 | Description               |
| -------- | ------------------------ | ------------------------- |
| **POST** | `/jwt/signup/`           | Create new user           |
| **POST** | `/jwt/login/`            | Get access/refresh tokens |
| **POST** | `/jwt/logout/`           | Blacklist refresh token   |
| **POST** | `/jwt/change-password/`  | Change password           |
| **POST** | `/jwt/bulid_in_login/`   | Built-in JWT login        |
| **POST** | `/jwt/bulid_in_refresh/` | Refresh access token      |
| **POST** | `/jwt/bulid_in_logout/`  | Built-in logout           |

### 🛠️ Utility Endpoints

| Method   | Endpoint            | Description                       |
| -------- | ------------------- | --------------------------------- |
| **GET**  | `/data/`            | Query data with params            |
| **POST** | `/data/`            | Add data with params              |
| **GET**  | `/find_movie/`      | Find movie by name and hall       |
| **POST** | `/new_reservation/` | Create reservation with new guest |
| **POST** | `/cookie/`          | Set HTTP-only cookies             |
| **GET**  | `/cookie/`          | Get cookie values                 |
| **POST** | `/github-webhook/`  | GitHub webhook receiver           |

---

## 📝 Database Models

### Movie

| Field        | Type             | Description                |
| ------------ | ---------------- | -------------------------- |
| `hall`       | CharField(10)    | Hall number/name           |
| `movie`      | CharField(50)    | Movie title                |
| `date`       | DateField        | Auto-updated date          |
| `created_by` | ForeignKey(User) | User who created the movie |

### Guest

| Field    | Type          | Description        |
| -------- | ------------- | ------------------ |
| `name`   | CharField(50) | Guest full name    |
| `mobile` | CharField(15) | Guest phone number |

### Reservation

| Field    | Type              | Description                                    |
| -------- | ----------------- | ---------------------------------------------- |
| `guests` | ForeignKey(Guest) | Reserved guest (One-to-One in current version) |
| `movies` | ForeignKey(Movie) | Reserved movie (One-to-One in current version) |

---

## 🔄 Data Relationships

```text
User (1) ----< Movie (M)         (created_by)
Guest (1) ----o Reservation (1)  (guests)
Movie (1) ----o Reservation (1)  (movies)
```

---

## 💻 API Usage Examples

### 1. Movie API (APIView Pattern)

#### Create Movie

```http
POST /movie/
Authorization: Bearer <jwt_token>
Content-Type: application/json

{
    "hall": "Hall 1",
    "movie": "Inception"
}
```

**Response:**

```json
{
    "id": 1,
    "hall": "Hall 1",
    "movie": "Inception",
    "date": "2026-08-19",
    "created_by": 1
}
```

#### Get Movies (Paginated)

```http
GET /movie/?page=2&page_size=10
Authorization: Bearer <jwt_token>
```

**Response:**

```json
{
    "count": 25,
    "next": "http://localhost:8000/movie/?page=3",
    "previous": "http://localhost:8000/movie/?page=1",
    "results": [
        {
            "id": 6,
            "hall": "Hall 2",
            "movie": "The Matrix",
            "date": "2026-08-19",
            "created_by": 1
        }
    ]
}
```

#### Get Single Movie

```http
GET /movie/1/
Authorization: Bearer <jwt_token>
```

#### Update Movie

```http
PATCH /movie/1/
Authorization: Bearer <jwt_token>
Content-Type: application/json

{
    "hall": "Hall 3"
}
```

#### Delete Movie

```http
DELETE /movie/1/
Authorization: Bearer <jwt_token>
```

---

### 2. Guest API (Generic Views Pattern)

#### Create Guest

```http
POST /guest_generic/
Content-Type: application/json

{
    "name": "John Doe",
    "mobile": "01234567890"
}
```

**Response:**

```json
{
    "id": 1,
    "name": "John Doe",
    "mobile": "01234567890"
}
```

#### List Guests

```http
GET /guest_generic/
```

---

### 3. Reservation API (ViewSet Pattern)

#### Create Reservation

```http
POST /reservation_viewset/
Content-Type: application/json

{
    "guests": 1,
    "movies": 1
}
```

**Response:**

```json
{
    "id": 1,
    "guests": 1,
    "movies": 1
}
```

---

### 4. Authentication (JWT)

#### Signup

```http
POST /jwt/signup/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "SecurePass123!"
}
```

**Response:**

```json
{
    "message": "User created"
}
```

#### Login (Get Tokens)

```http
POST /jwt/login/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "SecurePass123!"
}
```

**Response:**

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIs...",
    "access": "eyJhbGciOiJIUzI1NiIs..."
}
```

#### Refresh Token

```http
POST /jwt/bulid_in_refresh/
Content-Type: application/json

{
    "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
```

**Response:**

```json
{
    "access": "eyJhbGciOiJIUzI1NiIs..."
}
```

#### Logout (Blacklist Refresh Token)

```http
POST /jwt/logout/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
```

---

### 5. Authentication (Token)

#### Signup

```http
POST /token/signup/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "SecurePass123!"
}
```

#### Login (Get Token)

```http
POST /token/login/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "SecurePass123!"
}
```

**Response:**

```json
{
    "message": "Logged in successfully",
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

#### Authenticated Request

```http
GET /movie_generic/
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

#### Logout

```http
POST /token/logout/
Authorization: Token <your_token>
```

---

### 6. Custom Endpoints

#### Find Movie

```http
GET /find_movie/
Content-Type: application/json

{
    "name": "Inception",
    "place": "Hall 1"
}
```

**Response:**

```json
[
    {
        "id": 1,
        "hall": "Hall 1",
        "movie": "Inception",
        "date": "2026-08-19",
        "created_by": 1
    }
]
```

#### Create Reservation with New Guest

```http
POST /new_reservation/
Content-Type: application/json

{
    "movie_name": "Inception",
    "movie_place": "Hall 1",
    "guest_name": "Jane Smith",
    "guest_mobile": "01123456789"
}
```

**Response:**

```json
{
    "id": 2,
    "guests": 2,
    "movies": 1
}
```

#### Data Query (GET)

```http
GET /data/?movie=1
```

**Response:**

```json
{
    "1": "Inception"
}
```

#### Data Create (POST)

```http
POST /data/?movie=1
Content-Type: application/json

{
    "hall": "Hall 5",
    "movie": "The Dark Knight"
}
```

---

### 7. Cookies Example

#### Set Cookie

```http
POST /cookie/
Content-Type: application/json

{
    "name": "John",
    "age": "30"
}
```

**Response:** Cookie set in browser.

#### Get Cookie

```http
GET /cookie/
```

**Response:**

```json
{
    "csrftoken": "...",
    "sessionid": "...",
    "name": "John",
    "age": "30"
}
```

---

### 8. GitHub Webhook

#### Receive Webhook Payload

```http
POST /github-webhook/
Content-Type: application/json

{
    "head_commit": {
        "message": "Updated code"
    }
}
```

**Response:**

```json
{
    "status": "ok",
    "commit_message": "Updated code"
}
```

---

## 🔧 Configuration

### JWT Settings

```python
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
```

### DRF Settings (Global)

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}
```

### Database

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### Installed Apps

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]
```

---

## 🎯 API Implementation Comparison

| Pattern            | Files                  | Complexity | Use Case                 |
| ------------------ | ---------------------- | ---------- | ------------------------ |
| **Function-Based** | `views.py`             | Low        | Simple endpoints         |
| **APIView**        | `views.py`             | Medium     | Full control needed      |
| **Mixins**         | `views.py`             | Medium     | Reusable CRUD operations |
| **Generic Views**  | `views.py`             | Low-Medium | Standard CRUD operations |
| **ViewSets**       | `views.py` + `urls.py` | Low        | Automatic routing        |

---

## 🔐 Authentication Comparison

| Method      | Token Storage         | Use Case                    |
| ----------- | --------------------- | --------------------------- |
| **Session** | Cookies (server-side) | Web apps with login UI      |
| **Token**   | Authorization Header  | Mobile apps, external APIs  |
| **JWT**     | Authorization Header  | Stateless, scalable systems |

---



## 🐛 Troubleshooting

### Common Issues

**1. "Authentication credentials were not provided"**

* Include token in Authorization header.
* Format: `Bearer <token>` or `Token <token>`.

**2. "Invalid token"**

* Token may be expired (JWT: 5 minutes).
* Refresh token and try again.

**3. CSRF Token Missing (Session Auth)**

* Include `X-CSRFToken` header.
* Or use `@csrf_exempt` on views.

**4. Pagination Not Working**

* Use `?page=2` in URL.
* Change `PAGE_SIZE` in settings.

**5. "User not found"**

* Ensure user exists in database.
* Check username case sensitivity.

---

## 🔒 Security Best Practices

1. **Always use HTTPS in production**
2. **Store JWT secrets securely** in environment variables
3. **Set short-lived access tokens** (5 minutes)
4. **Implement token rotation** (refresh tokens)
5. **Use HTTP-Only cookies** for sensitive data
6. **Validate all input data** in serializers
7. **Use CSRF protection** for session-based auth
8. **Blacklist tokens** on logout

---

## 📦 Dependencies

```text
asgiref==3.8.1
Django==5.1.5
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
PyJWT==2.9.0
sqlparse==0.5.3
tzdata==2025.1
virtualenv==20.28.0
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is proprietary and confidential.

---

## 👨‍💻 Author

**Ebrahim Alfeky**

---

## 🙏 Acknowledgments

* Django REST Framework community
* SimpleJWT for JWT authentication
* DRF Authtoken for token authentication

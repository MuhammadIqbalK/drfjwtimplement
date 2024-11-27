# Simple JWT Implementation with Django Rest Framework

This project demonstrates how to implement **JSON Web Token (JWT)** authentication in a Django application using the **Django Rest Framework (DRF)** and the **Simple JWT** library. It provides a basic setup for creating secure APIs with token-based authentication.

## Features ✅
- **JWT Authentication**: Secure token-based authentication for your API endpoints.
- **Django Rest Framework Integration**: Full integration with DRF for building RESTful APIs.
- **User Registration & Login**: User registration, login, and token management.
- **Protected Endpoints**: Example of protected API endpoints that require a valid JWT token.

## Prerequisites 🐍

Before you begin, ensure you have met the following requirements:
- Python 3.8+ installed on your machine.
- A virtual environment for your project (optional but recommended).
- Django and Django Rest Framework installed.
- Simple JWT package installed.

## Installation 🚀

1. **Clone this repository:**
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
2. **Create a virtual environment:**

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    Install the required dependencies:
    
    pip install -r requirements.txt
    Set up the database:

3. **Run the migrations to set up the necessary tables:**

    python manage.py migrate
    Create a superuser (optional but recommended for testing):
    
    python manage.py createsuperuser
    Start the development server:

    python manage.py runserver

## Configuration 🛠️

 1. **Install Simple JWT: In your Django project, you will need to add rest_framework_simplejwt to your INSTALLED_APPS in settings.py.**

    `INSTALLED_APPS = [
        ...
        'rest_framework',
        'rest_framework_simplejwt',
    ]`
 2. **Update the Authentication Settings: In settings.py, configure REST_FRAMEWORK to use JWT authentication.**

    `REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
    }`
 3. **URL Configuration: Add URLs for obtaining the JWT token and refreshing it in your urls.py.**

    `from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView`
    
    `urlpatterns = [
        ...
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]`

 ## Usage 🖥️
 
  **Obtain a JWT Token:**
  
  - To get a JWT token, make a POST request to the /api/token/ endpoint with the following payload:
  
  `{
      "username": "your_username",
      "password": "your_password"
  }`
  
  A successful response will return an access and refresh token:
  
  `{
      "access": "your_access_token",
      "refresh": "your_refresh_token"
  }`
  
  Access Protected Endpoints:
  
  - To access protected endpoints, include the access token in the Authorization header as a Bearer token.
  
  Example:
  
  `curl -H "Authorization: Bearer your_access_token" http://127.0.0.1:8000/api/protected-endpoint/`
  
 ## Example Endpoints 🔥

  - `POST /api/register/` - Create the userAccount.
  - `POST /api/login/` - Obtain a JWT token & Login to userAccount.
  - `POST /api/login/refresh/` - Refresh the JWT token using the refresh token.
  - `GET /api/protected-endpoint/` - A protected endpoint that requires authentication.

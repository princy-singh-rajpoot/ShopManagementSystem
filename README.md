# Shop Management System

## Project Overview

Shop Management System is a web-based e-commerce platform that allows users to browse, search, and purchase products online. The platform provides an admin interface for managing products, orders, and users. 

## Features

- User authentication (signup, login, logout)
- User profile management
- Product listing and details
- Search and filter products
- Shopping cart functionality
- Order management
- Admin dashboard for managing products, orders, and users

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default), can be configured to use other databases
- **Libraries and Frameworks:** Bootstrap, jQuery

## Requirements

- Python 3.8 or higher
- Django 3.2 or higher
- Virtualenv (optional but recommended)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/princy-singh-rajpoot/ShopManagementSystem.git
   cd shop-management-system

2. **Create and activate a virtual environment:**

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the dependencies:**

    pip install -r requirements.txt

4. **Apply migrations:**

    python manage.py migrate

5. **Create a superuser:**

    python manage.py createsuperuser

6. **Collect static files:**

    python manage.py collectstatic

7. **Run the development server:**

    python manage.py runserver
    Visit http://127.0.0.1:8000/ to see the application in action.

**Usage**

    Admin Dashboard: Access the admin dashboard at http://127.0.0.1:8000/admin/ using the superuser credentials.
    User Registration and Login: Register a new user account or log in with existing credentials to start shopping.
    Browse Products: Explore the product catalog, add items to the shopping cart, and proceed to checkout.
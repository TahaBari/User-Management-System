# User Management System

A Flask-based User Management System with features for user authentication, registration, and profile management.

## Features

- User Registration
- User Login/Logout
- Profile Management (Edit profile information)
- Secure Password Handling
- MySQL Database Integration
- Bootstrap UI

## Technologies Used

- Flask
- Flask-Login (User session management)
- Flask-SQLAlchemy (Database ORM)
- MySQL (Database)
- Bootstrap 5 (Frontend styling)
- Jinja2 (Template engine)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/User-Management-System.git
cd User-Management-System
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a MySQL database:
```sql
CREATE DATABASE user_management;
```

5. Create a `.env` file in the project root and add your configuration:
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=mysql+pymysql://username:password@localhost/user_management
```

6. Run the application:
```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000`

## Project Structure

```
User-Management-System/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── profile.html
│       └── register.html
├── config.py
├── run.py
├── requirements.txt
└── .env
```

## Usage

1. Register a new account
2. Log in with your credentials
3. View and edit your profile information
4. Log out when finished

## Security Features

- Password hashing using Werkzeug's security functions
- CSRF protection for forms
- Secure session management
- SQL injection protection through SQLAlchemy
- Input validation and sanitization

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
# Personalized Learning Platform 🎓

## About the Project

The Personalized Learning Platform is a Python-based desktop application developed using Tkinter and MySQL. It aims to provide a personalized learning experience by allowing users to select courses, identify their learning levels, receive learning recommendations, and track their learning progress.

## Features

- User Registration and Login
- Course Selection
- Learning Level Identification
- Personalized Learning Recommendations
- Learning Progress Tracking
- MySQL Database Connectivity

## Technologies Used

- **Programming Language:** Python
- **GUI:** Tkinter
- **Database:** MySQL
- **IDE:** PyCharm

## Project Structure

```text
Personalized-Learning-Platform/
│
├── app.py
├── db_setup.py
└── README.md
```

## Installation and Setup

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate to the project folder:

```bash
cd Personalized-Learning-Platform
```

3. Install the MySQL connector:

```bash
pip install mysql-connector-python
```

4. Start your MySQL server.

5. Configure your database connection in the project.

6. Run the application:

```bash
python app.py
```

## Database

The application uses MySQL to store user information and learning progress.

**Database Name:** `learning_platform`

**Tables:**
- `users` – Stores user registration and login details.
- `progress` – Stores users' course progress.

## Future Enhancements

- AI-based learning recommendations
- More interactive learning modules
- Performance analytics and reports
- Improved user interface

## Author

Developed as a Python application project using Tkinter and MySQL.

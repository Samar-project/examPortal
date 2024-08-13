# Online Exam System # examPortal
This is project *examPortal* is an online exam management system built with Django, designed to facilitate the administration of exams and user registrations. This project allows users to register, log in, and take exams based on their selected subjects. It also includes an admin panel for managing users, subjects, and exams.

## Features

- **User Registration & Authentication**: Users can register, log in, and reset passwords.
- **Exam Management**: Admins can create subjects, add questions, and manage exams.
- **Responsive Design**: User-friendly interface that works on both desktop and mobile devices.
- **Admin Panel**: Manage users, exams, and subjects through the Django admin interface.

## Installation

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/Samar-project/examPortal](https://github.com/Samar-project/examPortal.git)
   cd examPortal
   python manage.py flush --for deletinng existing database data.

Apply Migrations
python manage.py migrate

Create a Superuser
python manage.py createsuperuser

Run the Development Server
python manage.py runserver

Access the Application
Visit http://127.0.0.1:8000/ in your web browser to view the home page.

Access the admin panel at http://127.0.0.1:8000/admin/

Usage

For Users:
Register as a new user or log in using an existing account.
Once logged in, select a subject and take an exam.
View your exam results upon completion.

For Admins:
Log in to the admin panel using the superuser credentials.
Manage users, subjects, and exams from the admin dashboard.
Project Structure

online-exam-system/
│
├── examPortal/
│   ├── migrations/          # Database migrations
│   ├── static/              # Static files (CSS, JavaScript, Images)
|   |    ├── examPortal/
|   |        ├── css/
│   ├── templates/           # HTML templates
|   |    ├── admin/          # Admin related HTML templates
|   |    ├── examPortal/     # examPortal related HTML templates
│   ├── admin.py             # Admin configurations
│   ├── apps.py              # Application configurations
│   ├── models.py            # Models for the database
│   ├── tests.py             # Test cases
│   ├── urls.py              # URL routing
│   └── views.py             # View functions
├── onlineExam/
│   ├── __init__.py          
│   ├── asgi.py            
│   ├── settings.py          # All the settings and Configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py             
│
├── manage.py                # Django management script
└── README.md                # Project documentation


Contributing
Contributions are welcome! If you find any issues or want to add new features, please submit a pull request or open an issue.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the Django community for providing comprehensive documentation and support.
Icons by Font Awesome.
Template inspiration from Bootstrap.


### Explanation:
- **Installation**: Clear steps to set up the project locally.
- **Usage**: Instructions on how users and admins can interact with the application.
- **Project Structure**: Helps contributors and other developers understand the organization of the codebase.
- **Contributing**: Encourages collaboration by explaining how to contribute to the project.
- **License**: The standard section for open-source projects.







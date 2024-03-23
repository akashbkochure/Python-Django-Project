django.akashbkochure.online/admin
django.akashbkochure.online/portfolio/job


# Python-Django-Project #

### Frontend Backend Postgress-DB loabancer waf cloudwatch logs alarm route53 acm dns-mapping with hostinger Project ###

Frontend Language: 
Python, specifically Django framework, is used for the frontend. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Python is used as the frontend language. In Django projects, Python is not only used for backend logic but also for generating dynamic content and rendering HTML templates. template/portfolio/index.html: This file is likely a part of your Django project's template system. In Django, templates are used to generate HTML dynamically. The portfolio directory indicates that this HTML file is related to the portfolio section of your website. The index.html file is often the main or landing page of a section. This file is likely a Django template used to render the homepage or index page of your portfolio application.

Backend Language: 
Python, again using Django, serves as the backend language. This includes handling requests, processing data, interacting with the database, and generating dynamic content for the frontend. Django is used as the backend language. It's a high-level Python web framework that facilitates rapid development and follows the Model-View-Template (MVT) architecture, handling data models (models.py), views (views.py), and templates (HTML files).

Database: 
PostgreSQL is used as the database management system (DBMS) for storing and retrieving data. It's a powerful, open-source relational database known for its reliability, robust features, and support for advanced SQL functionalities. PostgreSQL is used as the database management system. Django integrates well with PostgreSQL and provides an Object-Relational Mapping (ORM) layer for interacting with the database using Python objects.


# Admin Interface UI (publicip:8000/admin):

Login Page: You can log in with the superuser credentials you created (akashbkochure in your case).
User Management: Add, edit, and delete user accounts.
Group Management: Manage user groups and their permissions.
Role Management: Assign roles to users or groups.
Permission Management: Define and manage permissions for different actions in the system.
Job Management: If your project includes a Job model, you might be able to manage job listings, descriptions, images, etc., depending on how the admin interface is configured.

# Portfolio Section (App Home Page) (publicip:8000/portfolio/job):

This section likely displays a list of jobs or portfolio items.
You may be able to view job details, descriptions, and associated images.
Depending on the functionality implemented, users may also have options to add, edit, or delete portfolio items or jobs.
These pages provide an interface for managing your application's data and content, making it easier to perform CRUD (Create, Read, Update, Delete) operations on various resources such as users, jobs, and portfolio items.

# Project Workflow:

Update System and Install Git: This step ensures your system is up to date and installs Git for version control.

Clone Django Project: Cloning the Django project repository from GitHub (https://github.com/akashbkochure/Python-Django-Project.git) to your local environment.

Install Python3: If not already present, Python 3 is installed as it's required for Django.

Install Django and Dependencies: Django and related packages like psycopg2-binary (for PostgreSQL database) and pillow (for image processing) are installed using pip3.

Install PostgreSQL: Installing PostgreSQL database server and setting it up for your Django project.

Configure Django Settings: Editing Django's settings file (akash/settings.py) to configure database settings (e.g., username, password, database name, host).

Initialize Database: Creating the PostgreSQL database for your project, running migrations, and creating a superuser for admin access.

Run Django Server: Starting the Django development server (python3 manage.py runserver) to run your project locally or on an EC2 instance.

Make Server Publicly Accessible: Configuring Django to run on a publicly accessible IP and port (0:8000) and updating allowed hosts in settings.

Restart PostgreSQL Service: Restarting the PostgreSQL service after making configuration changes.

This workflow sets up your Django project, initializes the database, and runs the development server either locally or on a server like EC2 for deployment.


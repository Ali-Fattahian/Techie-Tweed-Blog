# Techie Tweed

### Description

Techie Tweed is a blog focused on programming related articles.

### Features

- Users can write articles and include images if they want using ckeditor, a rich text editor.
- Users can add tags to posts they have created.
- Users have to sign up with email, username and password.
- Users can reset their password using the email they have provided.
- Users can edit their profile, have a bio, profile picture and share their social media accounts which will be shown with their icons.
- Users can store their favorite posts in a session and have access to all of them (session based bookmark system).
- Admins can manage users and articles.
- There is a weekly automatic back up system using cron and dbbackup package.
- Posts are shown with pagination for a cleaner ui.

### Technologies and libraries used

- Django
- Postgres
- psycopg2-binary
- dj-database-url
- Cloudinary
- Django cloudinary storage
- Django white noise
- django-ckeditor
- django-dbbackup
- Pillow
- gunicorn
- python-dotenv

### How to run the project

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Ali-Fattahian/Techie-Tweed-Blog
```

Create a virtual environment to install dependencies in and activate it:

```sh
python3 -m venv env
source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Since this project is in production, you have to change settings to dev to work with it, so open settings.py,

Use an online tool like *https://djecrety.ir/*
to get a new secret key for the project.

Set DEBUG=True,

Create a database and set DATABASES settings to the one you created,

either remove cloudinary settings and apps from installed_apps or set the configuration to your own account, at last set the email config to your email.

once you did all of that,

```sh
python manage.py makemigrations
python manage.py migrate
```

To create the tables in your database.

```ssh
python manage.py runserver
```

to run the server.

You can navigate to
`http://localhost:8000`
to explore the website.

You can navigate to
`http://localhost:8000/users/register`
to create an account

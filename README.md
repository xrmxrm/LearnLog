This project is based on Python Crash Course by Eric Matthes, third edition, from No Starch Press. Here is Eric's spec:

>We’ll write a web app called Learning Log that allows users to log the topics they’re interested in and make journal entries as they learn about each topic. The Learning Log home page will describe the site and invite users to either register or log in. Once logged in, a user can create new topics, add new entries, and read and edit existing entries.

# Setup

  1. Create virtual environment `~/V/ll_env` and activate it.
  2. Upgrade pip and use it to install Django 5.0.3
  3. `django-admin startproject ll_project .`

     This creates `settings.py`, `urls.py`, `wsgi.py` and a few other files.

  4. `python manage.py migrate`

     This builds the database (SQLite) in `db.sqlite3`.

  5. `python manage.py runserver`

     This starts the development server running on `localhost:8000`:

     ```
     Watching for file changes with StatReloader
     Performing system checks...

     System check identified no issues (0 silenced).
     March 10, 2024 - 22:08:55
     Django version 5.0.3, using settings 'll_project.settings'
     Starting development server at http://127.0.0.1:8000/
     Quit the server with CONTROL-C.

     ```
     Keep the server running in its own terminal window, and in another, continue development.

   6. `python manage.py startapp learning_logs` 

      This creates the app's infrastructure.
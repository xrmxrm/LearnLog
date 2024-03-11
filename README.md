This project is based on Python Crash Course by Eric Matthes, third edition, from No Starch Press. Here is Eric's spec:

>We’ll write a web app called Learning Log that allows users to log the topics they’re interested in and make journal entries as they learn about each topic. The Learning Log home page will describe the site and invite users to either register or log in. Once logged in, a user can create new topics, add new entries, and read and edit existing entries.

# Setup

  1. `~/V$ python -m venv ll_env`
  
     This creates a virtual environment `~/V/ll_env`.

  2. source ~/V/ll_env/bin/activate

     To activate it, execute 

  3. `django-admin startproject ll_project .`
  
     This installs Django 5.0.3
  
  4. `django-admin startproject ll_project .`

     This starts the project and creates `settings.py`, `urls.py`, `wsgi.py` and a few other files.

  5. `python manage.py migrate`

     This builds the database (SQLite) in `db.sqlite3`.

  6. `python manage.py runserver`

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

   7. `python manage.py startapp learning_logs` 

      This creates the app's infrastructure in a folder called `learning_logs`.

# App development

In `models.py`, add a Topic class. In `settings.py` in the project directory, add `learning_logs` to the installed apps. Then run 

   ```python manage.py makemigrations learning_logs```

Then apply the migration:

   ```python manage.py migrate```

## Admin site and superuser

Exexute `python manage.py createsuperuser` and follow the prompts.

To register Topic with the admin site:

```
from .models import Topic

admin.site.register(Topic)
```
## Add Entry to model

Edit `models.py`, then run the familiar pattern:

```
python manage.py makemigrations learning_logs
python manage.py migrate
```

Then register Entry on the admin site by editing `admin.py`.

The server notices the change, and the site updates automatically.

## Interactive shell

Execute `python manage.py shell` to start an interactive shell.

## Pages

Pages require URLs, views, and templates. URLs are defined by patterns which determine which page to return. The page is defined by a view, which may use a template.

### URLs

Start by adding `path('', include('learning_logs.urls')),` to the `urls.py` file in the `ll_project` directory. That causes any URL other than the admin ones to use the `urls.py` file in the `learning_logs` directory.

In `learning_logs/urls.py`, the `urlpatterns` list begins with the home page:

   ```path('', views.index, name='index'),```

The first arg matches the base URL (`localhost:8000` for now). The second says to call the `index` function in the `views.py` module. The third gives this URL pattern a name.

### Views

The index function in views.py has the following code:

```
def index(request):
    return render(request, 'learning_logs/index.html')

```

This passes the `request` object and the 'learning_logs/index.html' template to the `render` function.

### Templates


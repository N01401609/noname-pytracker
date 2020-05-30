# Installing Django
First make sure you have python installed
Check the version of python you have
```python
    $ python --version
```

Now we can install django
```python
		$ python -m pip install Django
```
Just like with python, we can check the version that you have
```python
		$ python -m django --version
```
# Creating a project
From the command line, cd into a directory where you’d like to store your code, then run the following command:
```python
	$ django-admin startproject mysite
```
This will create a mysite directory in your current directory, creating the following:
> mysite/ -- this is the root container for the project
    manage.py  -- this is the command-line utility that interacts with the django project
    mysite/ -- this is the Python package for the project
        __init__.py -- this tells Python that this should be considered a Python package
        settings.py -- settings/config for the project
        urls.py -- thinks of this as your table of contents for the Django-powered site
        asgi.py -- entry point for ASGI-compatible web servers
        wsgi.py -- entry point for WSGI-compatible web servers


# The development server
Change into the outer mysite directory, and run the following commands:
```python
	$ python manage.py runserver
```
This will start the Django development server, a lightweight Web server written purely in Python. Click the link in the outputted text (something like: Starting development server at http://127.0.0.1:8000/) 
You’ll see a “Congratulations!” page, with a rocket taking off. It worked!
If your port is not available you can change server ports 
```python
	$ python manage.py runserver 8080
```

# Creating an app
Now that your environment – a “project” – is set up, you’re set to start doing work.  Your apps can live anywhere on your Python path.  To create your app, make sure you’re in the same directory as manage.py and type this command:
```python
	$ python manage.py startapp <appname>
```
This will create a directory based on your <appname>, and populate the following layout:
>
>   <appname>/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py

This will house the <appname> application

# Write a view
Open the file views.py and put the following Python code in it:
```python

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the <appname> index.")
```

Now  create a URLconf in the <appname> directory, create a file called urls.py.  The urls.py file should include the following code:
```python	
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
Now in the root folder , mysite.url, insert the following code in the url.py file:
```python
from django.contrib import admin

from django.urls import include, path

urlpatterns = [
    path('<appname>/', include('<appname>.urls')),
    path('admin/', admin.site.urls),
]
```

You have now wired an index view into the URLconf. Verify it’s working with the following command:
```python
$ python manage.py runserver
```
Go to http://localhost:8000/<appname>/ in your browser, and you should see the text “Hello, world. You’re at the <appname> index.”, which you defined in the index view.
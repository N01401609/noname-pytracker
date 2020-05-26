# Notes First Hello World Program Django
## 1. Installing Python and Pycharm into computer
- Install version 3.7 in mac
- Download Pycharm Professional
- Setup Compressor python, this can be changed for every project
- To set up default configure on first page before starting project
- Command to print Hello World into the console with plain python is the following

        print("Hello World")
 - In order to run this program you can go to the console, cd into the folder that has the py file and run the command 
 line 
 > python nameoffile.py 
  
## 2. Django Project Setup
### In the Command Line
> django-admin start project name

### Directly in Pycharm
- When creating a new project select django on the list of options on the side
- Select the virtual enviroment with the interpreter you wish to use

### Files found in Django 
These files are:

- The outer mysite/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
- manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
- The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
- mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
- mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
- mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
- mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See How to deploy with ASGI for more details.
- mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.

### The development server
- On settings.py insert the following code line

        ALLOWED_HOSTS = ['*']

- This will allow us to use the localhost as the server
 - Run server line is the following (starts the server)
 >python manage.py runserver 127.0.0.1:8080

## 3. Start an Application
Each application you write in Django consists of a Python package that 
follows a certain convention. Django comes with a utility that automatically 
generates the basic directory structure of an app, so you can focus on writing 
code rather than creating directories.

On command line type:
>python manage.py startapp test1

### Write first view
- open the views.py file under the test1 application folder and write the following code

        from django.http import HttpResponse
        def index(request):
            return HttpResponse("Hello, world. You're at the polls index.")
            
- This will render the page into the web browser
### Now Create the re-direct URLS
- Now create a page inside the test1 folder called urls.py and paste the following:
        
        from django.urls import path
        
        from . import views
        
        urlpatterns = [
            path('', views.index, name='index'),
        ]
        
 
 - In the above piece of code the . is the root folder test1 and views.index
 represents the function index that we created inside the view document
 
 ### Linking the test1 urls to the main urls
- Next we are going to link the request to the urls.py
- Now link it to the main urls.py found in the sub-folder DJangoHelloWorld
- Add the following line to the the main folders urls.py 
 
         from django.contrib import admin
         from django.urls import path , include
         
 - we are adding include into the path so we can use it on the path below
         
         urlpatterns = [
         path('admin/', admin.site.urls),
         path('test1/', include('test1.urls')),
         ]
- the test1 path is linking this urls to the urls in test1

### Restart the server and see the hello world example
- Finally restart the server
>python manage.py runserver 127.0.0.1:8080

- Now when going to the browser we put the following
>http://127.0.0.1:8080/test1/

-- YOU ARE DONE! YOU SHOULD BE ABLE TO SEE THE MESSAGE YOU WROTE ON THE VIEWS ON YOUR BROWSER



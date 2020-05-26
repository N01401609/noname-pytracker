#Hello World with Django

##Creating a Project
- Create New > Django > virtualenv to create environment to work with
- Configure interpreter with Python3.7 and Django server (run in browser)


## How do files work together?
####settings.py
- holds information about yoru database, which engine and db name you are referencing
- For tutorial, using sqlelite3 database, to change to MySQL for project, replace sqlelite3 with MYSQL
-If creating a new app, need to add it to the INSTALLED_APPS folder at the end of the list
####models.py
- "a single, definitive source of information about your data"
- similar to ASP.NET MVC, this is how we map out the database
- tables are mapped out using classes:
~~~ 
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
~~~~
translates to: 
~~~ 
CREATE TABLE myapp_person (
    "id" serial NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL
);
~~~
####manage.py
- here is where we run migrations - runserver from manage.py, open the file in the editor and enter OPTION + R 
- This will open a manage.py@sitename console and begin running django server for you to work with
- RESULT: a page will open in the default browser either saying error or success
- This console is where you would also create database migrations - running makemigrations command and sqlmigrate command
- Final command: migrade will create the database you will work with
####urls.py
- in the main project folder, you need to add your url paths so that they can be followed and load in the browser
- this file works using include('app_name.urls')) - this calls to the url file in the app directory
- in the app directory, you need to  specify your url patterns, example:
~~~ 
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
~~~
- your urls file works with your views! Don't forget to add a new url pattern every time you add a new view - otherwise 
won't be able to see the front end of the file
####views.py
- These are built in your app folder
- start with importing HttpResponse
- define what your request is, example:
~~~ 
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
~~~
- This gives a front end view to a request for [localhost]/index/
####Templates Directory
- here you can code templates which will work with views
- IMPORTANT to ensure you have the right import statements when working with templates. Include:
~~~
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import [models you need here]
~~~
- Now we need to give the view more information to work with than just the string we want to print out. Index view becomes:
~~~
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
~~~
- index.html is going to be what we call our template (right click templates, click add file)
- in this html file we can code what the page will look like. Documentation example below:
~~~
{% load staticfiles %}
<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />
{% if latest_question_list %}
           <ul>
    {% for question in latest_question_list %}
           <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
    {% endfor %}
       </ul>
{% else %}
           <p>No polls are available.</p>
{% endif %}
~~~
###Running your django server
- "Add Configuration..." button at the top -> click + -> django
- Give server a name
- Make sure that Run Browser checkbox is selected
- Add the file path you want to open as soon as you run the server ([host]/admin/ or [host]/hello_world/)
- to launch, CONTROL + R and it will run the server and open the browser
- If you have done everything correctly, you will have an error message 0 in your console, and the requested path will load
- If you receive TemplateNotFound error, you have done something incorrectly - your files aren't talking to each other the way they should
- Check import statements, and ensure everything is connected



## Notes
some commands to run the server
--
>django-admin startproject 'project name'
>cd 'project name'
>python manage.py runserver


//now run the server from the given address

- [ ] create you app now in the project
 -- in the another terminal
>cd 'project name'
>python manage.py startapp 'app name'


run the installed app or models 
>python manage.py migrate


now if you want to add your classes 
>python manage.py makemigrations 'app name' in which you wanna add the migrations
>python manage.py sqlmigrate music 'migration number'

it will create the tables for you

again run the migration as you did previously
>python manage.py migrate

* now if you wanna see the value of the database 
* open the windows shell on that folder where the manage.py is located
#### type:
>python manage.py shell
#### then
>form 'project name'.models import 'class name,(s)'
>'class name'.objects.all()
* for adding the value
> a = Comments(comments = "this is my first django project", username="jazz")
* now save it
>a.save()
* as there is only one value in it you can see it
>a.id
>a.comments
* again if you want to add the more values
>b = Comments()
>b.comments = "this is second comments"
>b.save()
* if you wanna update the value
>b.comments = "this is updated comment"
>b.save()

#### filter the vlaue
>Comments.objects.filter(id=2)
* or you can use the where query like
>Comments.objects.filter(username__startswith='jazz')

* for admin site
* we have to create username and password
>python manage.py createsuperuser
* then set the username and password


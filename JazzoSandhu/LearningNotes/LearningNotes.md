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


https://www.youtube.com/watch?v=IU3LbtbmXXI

run the installed app or models 
>python manage.py migrate


now if you want to add your classes 
>python manage.py makemigrations 'app name' in which you wanna add the migrations
>python manage.py sqlmigrate music 'migration number'

it will create the tables for you

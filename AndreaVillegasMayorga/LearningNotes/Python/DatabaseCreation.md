##Migrations and model changes 

###three-step guide to making model changes:

- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.

The reason that there are separate commands to make and apply migrations is because 
you’ll commit migrations to your version control 
system and ship them with your app; they not only 
make your development easier, they’re also usable 
by other developers and in production.

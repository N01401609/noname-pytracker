# Database Creation

## three-step guide to making model changes:

### Creating a Model
- Create/Change your models (in models.py).
        from django.db import models
        
        class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

### Activate Models
- in settings.py add the following line of code:
 
        INSTALLED_APPS = [
        'polls.apps.PytrakerConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        ]
 
 ### Run Migrations 
1. Make Migrations 
>python manage.py makemigrations PyTraker
   - Run python manage.py makemigrations to create migrations for those changes
   - you will see:
   >Migrations for 'polls':
    polls/migrations/0001_initial.py
    >- Create model Question
    >- Create model Choice

2. Run Migrations
>python manage.py sqlmigrate PyTraker 0001
   - This runs the migration that is created 
   - you will see:
>   BEGIN;
--
-- Create model Question
--
CREATE TABLE "polls_question" (
    "id" serial NOT NULL PRIMARY KEY,
    "question_text" varchar(200) NOT NULL,
    "pub_date" timestamp with time zone NOT NULL
);
--
-- Create model Choice
--
CREATE TABLE "polls_choice" (
    "id" serial NOT NULL PRIMARY KEY,
    "choice_text" varchar(200) NOT NULL,
    "votes" integer NOT NULL,
    "question_id" integer NOT NULL
);
ALTER TABLE "polls_choice"
  ADD CONSTRAINT "polls_choice_question_id_c5b4b260_fk_polls_question_id"
    FOREIGN KEY ("question_id")
    REFERENCES "polls_question" ("id")
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");

>COMMIT;

3.Create migrations in database
> python manage.py migrate
- The reason that there are separate commands to make and apply migrations is because 
you’ll commit migrations to your version control 
system and ship them with your app; they not only 
make your development easier, they’re also usable 
by other developers and in production.

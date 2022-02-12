# Django Databases

If you wish to use another database, install the appropriate database bindings and change the following keys in the DATABASES 'default' item to match your database connection settings:

    ENGINE – Either 'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle'.

    NAME – The name of your database. If you’re using SQLite, the database will be a file on your computer; in that case, NAME should be the full absolute path, including filename, of that file.

    The default value, BASE_DIR / 'db.sqlite3', will store the file in your project directory.


Some of these applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:

    python manage.py migrate


## Creating models

By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

    python manage.py makemigrations polls


Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file polls/migrations/0001_initial.py. Don’t worry, you’re not expected to read them every time Django makes one, but they’re designed to be human-editable in case you want to manually tweak how Django changes things.

There’s a command that will run the migrations for you and manage your database schema automatically - that’s called migrate, and we’ll come to it in a moment - but first, let’s see what SQL that migration would run. The sqlmigrate command takes migration names and returns their SQL:

    python manage.py sqlmigrate polls 0001

The sqlmigrate command doesn’t actually run the migration on your database - instead, it prints it to the screen so that you can see what SQL Django thinks is required. It’s useful for checking what Django is going to do or if you have database administrators who require SQL scripts for changes.

Now, run migrate again to create those model tables in your database:

    python manage.py migrate


The migrate command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.


### three-step guide to making model changes:

    - Change your models (in models.py).
    - Run python manage.py makemigrations to create migrations for those changes
    - Run python manage.py migrate to apply those changes to the database.


## Introducing the Django Admin

    python manage.py createsuperuser



# Django - Postgres - Redis - Celery - Docker

1. Create file `requirements.txt`

    Django>=2.2
    celery==4.4.1
    redis==3.4.1
    psycopg2>=2.7.5,<2.8.0


2. Create `Dockerfile`. Define your app’s environment with a `Dockerfile` so it can be reproduced anywhere.

    Docker can build images automatically by reading the instructions from a `Dockerfile`. A `Dockerfile` is a text document that contains all the commands a user could call on the command line to assemble an image. Using docker build users can create an automated build that executes several command-line instructions in succession.

3. Create `docker-compose.yml`. Define the services that make up your app in `docker-compose.yml` so they can be run together in an isolated environment.

    Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. 

4. Run `docker compose up` and the Docker compose command starts and runs your entire app. You can alternatively run `docker-compose up` using the docker-compose binary.


        docker-compose -f docker-compose.yml build

        ERROR: stderr=OpenSSL version mismatch

            Install Environment 
                    python3 -m venv .venv
                    source ./venv/bin/activate
                    pip install docker-compose

        docker-compose up --build
        docker-compose build

5. Create Django app project

        docker-compose run app sh -c "django-admin startproject app ."
        pip3 install -r requirements.txt
        pip3 install django
        django-admin startproject app .

6. Create Django core project

        docker-compose run app sh -c "django-admin startproject core"
        django-admin startproject core

7. Update app/settings.py

        INSTALLED_APPS = [
            ...
            'core',
        ]

8. Create the following folders/files
    
        core/management
        create file core/management/__init__.py
        create file core/management/commands/
        create file core/management/commands/__init__.py

T=00:10:42
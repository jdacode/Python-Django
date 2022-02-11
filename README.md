# Python-Django
Python-Django

    URL = Uniform Resource Locator 
    URL = http://  + duckduckgo.com + / main.html
    URL = Protocol + host           + document


    COMMANDS
        telnet duckduckgo.com 80
        GET / HTTP/1.1
        <enter>
        <enter>

    PYTHON
        Environment commands
            python3 -m venv .venv
            pip3 list
            which python3
            source ./venv/bin/activate

        Install packages
            pip3 install django
            python3 -m django --version
            pip3 uninstall django

        Project packages
            pip3 freeze
            pip3 freeze > requirements.txt
            pip3 install -r requirements.txt 
            
        Exit environment
            deactivate 

        remove virtual environment (delete folder)
            rm -rf venv/

## DJANGO Arch

![django_arch](/static/img/1.png)
<br><br>
![django_arch2](/static/img/3.png)
<br><br>


**URLs**: While it is possible to process requests from every single URL via a single function, it is much more maintainable to write a separate view function to handle each resource. A URL mapper is used to redirect HTTP requests to the appropriate view based on the request URL. The URL mapper can also match particular patterns of strings or digits that appear in a URL and pass these to a view function as data.

**View**: A view is a request handler function, which receives HTTP requests and returns HTTP responses. Views access the data needed to satisfy requests via models, and delegate the formatting of the response to templates.

**Models**: Models are Python objects that define the structure of an application's data, and provide mechanisms to manage (add, modify, delete) and query records in the database.

**Templates**: A template is a text file defining the structure or layout of a file (such as an HTML page), with placeholders used to represent actual content. A view can dynamically create an HTML page using an HTML template, populating it with data from a model. A template can be used to define the structure of any type of file; it doesn't have to be HTML!

## Django 

    Start Projects
        django-admin startproject <project_name> .

    Checking Django
        python3 manage.py check
        
    Run Django
        python3 manage.py runserver
        python manage.py runserver 8080
        python manage.py runserver 0:8000
            0 is a shortcut for 0.0.0.0

    Start App
        python3 manage.py startapp playground

    
## Django Files

    mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py



**mysite/**: The outer mysite/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

**manage.py**: A command-line utility that lets you interact with this Django project in various ways.

**mysite/**: The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

**mysite/\_\_init\_\_.py**: An empty file that tells Python that this directory should be considered a Python package. The **\_\_init\_\_.py** files are required to make Python treat directories containing the file as packages. This prevents directories with a common name, such as string, unintentionally hiding valid modules that occur later on the module search path. In the simplest case, **\_\_init\_\_.py** can just be an empty file, but it can also execute initialization code for the package or set the **\_\_all\_\_** variable, described later.

**mysite/settings.py**: Settings/configuration for this Django project. Django settings will tell you all about how settings work.

**mysite/urls.py**: The URL declarations for this Django project; a “table of contents” of your Django-powered site.

**mysite/asgi.py**: An entry-point for ASGI-compatible web servers to serve your project. ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.

**mysite/wsgi.py**: An entry-point for WSGI-compatible web servers to serve your project. WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.


## INCLUDE

The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

When to use include()

You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.


## Projects vs. apps

What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.


## Tools 
    
    VSCODE
        Environment:

            {
                "python.pythonPath": "PYTHON/Python-Django/02-storefront/.venv/bin/python3",
                "terminal.integrated.cwd": "PYTHON/Python-Django/02-storefront/"
            }
        
        Debugging:

            Run and Debug [icon] > create a launch.json > Workspace > Python > Django > launch.json > program > path to manage.py

                "program": "${workspaceFolder}/PYTHON/Python-Django/02-storefront/manage.py",
                "args": [
                    "runserver",
                    "9000" ----> [local port]
                ],

    
    
    
    DJANGO DEBUG TOOLBAR
        Installation:
            https://django-debug-toolbar.readthedocs.io/en/latest/installation.html

            python -m pip install django-debug-toolbar

            
            > settings.py:

                INSTALLED_APPS = [
                    # ...
                    'debug_toolbar',
                    # ...
                ]

                MIDDLEWARE = [
                    # ...
                    'debug_toolbar.middleware.DebugToolbarMiddleware',
                    # ...
                ]

                INTERNAL_IPS = [
                    # ...
                    '127.0.0.1',
                    # ...
                ]


            > urls.py:

                from django.urls import include, path

                urlpatterns = [
                    # ...
                    path('__debug__/', include('debug_toolbar.urls')),
                ]    

            
            > .html

                <html>
                    <body>
                        <!--
                            Code
                        -->
                    </body>
                </html>


> DOTADIW
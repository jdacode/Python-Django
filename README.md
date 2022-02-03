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

## Django 

    Start Projects
        django-admin startproject <project_name> .

    Checking Django
        python3 manage.py check
        
    Run Django
        python3 manage.py runserver

    Start App
        python3 manage.py startapp playground

    
    
    
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
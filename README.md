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

> T=00:25:00
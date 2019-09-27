# First Example - xml

- Added 2 files to test:

    - mect.xml
    - curso.xsd

- When validation fails, it is created a log file with errors.

## Requirements

- Python 3

- lxml

**Opcional**

- pycharm

- Django==2.2.5

## Run - terminal

1. Create a venv:

    `python3 -m venv venv`

    `source venv/bin/activate`

2. Install lxml

    `sudo pip install lxml==4.4.1`

3. Run xml_proc.py

    `python3 xml_proc.py`

## Run - django project

1. Create venv

2. Install Django

    `pip install Django==2.2.5`

3. Create Django project in Pycharm

    -  Existing interpreter 

        Interpreter: Python 3.7

        Template language: Django

        Template folder: app/templates

        Aplication name: app

4. `python manage.py migrate`

5. Run in pycharm bottom



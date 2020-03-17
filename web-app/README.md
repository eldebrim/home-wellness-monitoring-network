# Activity tracking web app

## Requirements
* Python 3.6+
* django 2.1+
* django-tables 2+
* django-basicauth 2+
* sqlite 3+
* git


## Installation
To start the website on port 8000, run these commands:
```
  python3 manage.py migrate
  python3 manage.py makemigrations polls
  python3 manage.py sqlmigrate polls 0001
  python3 manage.py migrate
  python3 manager.py runserver 0.0.0.0:8000
```

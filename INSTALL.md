cd ## Getting Started

1. get python 3 if you don't already have it
2. get pip (pip3 for python 3) if you don't already have it
3. get the virtualenv script with pip:
`pip install virtualenv`
4. create the virtual environment inside the project folder:
`mkvirtualenv env`
5. install front-end dependencies:
`npm install -python=python2.7`

might have to close and reopen the terminal between steps 3 and 4

## Typical Workflow

1. switch to project folder, run:
`source env/bin/activate`

so, activating will make "python" point to the local python and will make pip (python package manager) work with the local packages folder

2. once activated, install the project's python deps with:
`pip install -r localore/requirements-dev.txt`

3. if pip fails, it's probably because some system libs are missing, like for postgres install them and try again
4. run the db migrations:
`cd localore && python manage.py migrate`

5. create the superuser if you haven't already:
`python manage.py createsuperuser`

6. run the dev server:
`python manage.py runserver`

7. run grunt:
`grunt serve`

8. to get out of virtualenv:
`deactivate`


## Things that have to happen repeatedly:

1. you have to activate the python virt. environment first, whenever you work with the project

2. you have rerun migrations whenever you pull down changes that affect the DB

3. you have to reinstall python deps from the requirements file whenever the requirements file gets updated

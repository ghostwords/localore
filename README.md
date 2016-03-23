# Localore: Finding America


## Developer setup

1. Clone this project (with `--recursive` to pull down its git submodules).

2. Install Python 3, `pip`.

3. Install platform dependencies (feel free to skip this until you run into errors, probably in step 5):

	- Pillow: http://pillow.readthedocs.org/en/latest/installation.html#external-libraries
	- Python development package
	- libpq (Postgres) development package
	- ...

4. Optional, but recommended: Set up a Python 3 "virtual environment" for working on this project with `virtualenv`.

	1. get the virtualenv script with pip: `pip install virtualenv`
	2. close and reopen terminal
	3. create the virtual environment inside the project folder: `mkvirtualenv -p $(which python3) env`

5. Switch to the Wagtail/Django project directory: `cd localore`.

6. Install Python dependencies: `pip install -r requirements-dev.txt`. Install from `requirements-dev-linux.txt` on Linux. When we run into errors here, it probably means we forgot to document and/or install some platform dependency (see step 3).

7. Install front-end dependencies: `npm install --python=python2`

8. Copy [localore/.env](localore/localore/.env) to `localore/.env.local`. This is where your local environment variable settings (database config, etc.) go. See the arguments passed into `Env()` in [localore/settings.py](localore/localore/settings.py) for the list.

9. Set up the database: `python manage.py migrate`, then `createsuperuser`

10. Run the Django dev server: `python manage.py runserver`

11. Run Grunt to watch/recompile static resources, perform live reloading, etc.: `grunt serve`

	If the Django dev server isn't running on port 8000 (the default), you have to update livereload's proxy config in [Gruntfile.js](localore/Gruntfile.js).


## Things that have to happen repeatedly

1. you have to activate the python virt. environment first, whenever you work with the project

	- to activate, switch to project folder, run: `source env/bin/activate`
	- so, activating will make "python" point to the local python and will make pip (python package manager) work with the local packages folder

2. you have rerun migrations whenever you pull down changes that affect the DB

3. you have to reinstall python deps from the requirements file whenever the requirements file gets updated


## License

The source code is licensed under Mozilla Public License Version 2.0. This specifically does not cover any brand assets such as logos or trademarks. Brand assets cannot be reused without permission.

# Localore: Finding America


## Developer setup

1. Clone this project (with `--recursive` to pull down its git submodules).

2. Install Python 3 and `pip`.

3. Install platform dependencies (feel free to skip this until you run into errors, probably in step 6):

	- Pillow: http://pillow.readthedocs.org/en/latest/installation.html#external-libraries
	- Python development package
	- libpq (Postgres) development package
	- ...
	
	For example, on OS X with Homebrew: `brew install postgresql libmemcached`

4. Optional, but recommended: Set up a Python 3 "virtual environment" for working on this project with `virtualenv`.

	1. Get the virtualenv script with pip: `pip install virtualenv`
	2. Create the virtual environment inside the project folder: `virtualenv venv`
	3. Activate the environment: `source ./venv/bin/activate`. This has to happen each time you start work on the project.

5. Switch to the Wagtail/Django project directory: `cd localore`.

6. Install Python dependencies: `pip install -r requirements-dev.txt`. Install from `requirements-dev-linux.txt` on Linux. When we run into errors here, it probably means we forgot to document and/or install some platform dependency (see step 3). Another common issue is installing for the wrong Python version (2 instead of 3).

7. Install front-end dependencies: `npm install --python=python2`

8. Copy [localore/.env](localore/localore/.env) to `localore/.env.local`. This is where your local environment variable settings (database config, etc.) go. See the arguments passed into `Env()` in [localore/settings.py](localore/localore/settings.py) for the list.

9. Set up the database: `python manage.py migrate`, then `createsuperuser`

10. Run the Django dev server: `python manage.py runserver`

11. Run Grunt to watch/recompile static resources, perform live reloading, etc.: `grunt serve`

	If the Django dev server isn't running on port 8000 (the default), you have to update livereload's proxy config in [Gruntfile.js](localore/Gruntfile.js).

12. The primary HTML layout file, `base.html`, exists in `localore/static/html` and should be edited there. When grunt compiles, it will make a copy of this file with updated references to `localore/templates`. If you edit the file in `localore/templates` it will get overwritten next time grunt compiles.

## Packaging for deployment

`grunt build` will prepare front-end assets for deployment. It does the following:

1. Package vendor libraries from `bower_components`
2. Compile sass, compress resulting css file, and compress js files
3. Update references with cache-busting file revision numbers
4. and more!

Everything should be referenced from `static/dist` - you will need to also copy over `static/js` to account for `{% extra_js %}` blocks.

One outstanding issue is that `<img>` references scattered around the HTML won't take advantage of this because they are using the django `{% static %}` naming convention - for this reason `static/images` should also be included wherever assets are served just in case.

## Things that have to happen repeatedly

1. you have to activate the python virt. environment first, whenever you work with the project

	- to activate, switch to project folder, run: `source ./venv/bin/activate`
	- so, activating will make "python" point to the local python and will make pip (python package manager) work with the local packages folder

2. you have rerun migrations whenever you pull down changes that affect the DB

3. you have to reinstall python deps from the requirements file whenever the requirements file gets updated


## License

The source code is licensed under Mozilla Public License Version 2.0. This specifically does not cover any brand assets such as logos or trademarks. Brand assets cannot be reused without permission.

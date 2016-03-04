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

5. Install Python dependencies: `pip install -r localore/requirements-dev.txt`. When we run into errors here, it probably means we forgot to document and/or install some platform dependency (see step 3).

6. Set up the database: `./localore/manage.py migrate`, then `createsuperuser`

7. Run the dev server: `./localore/manage.py runserver`


## License

The source code is licensed under Mozilla Public License Version 2.0. This specifically does not cover any brand assets such as logos or trademarks. Brand assets cannot be reused without permission.

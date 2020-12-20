# IPTV-Manager

[![Lint and test](https://github.com/bjakushka/iptv-manager/workflows/Lint%20and%20test/badge.svg?branch=main)](https://github.com/bjakushka/iptv-manager/actions?query=workflow%3A%22Lint+and+test%22)

Flask-based app for managing IPTV sources

Minimum required version of python: 3.8

### How to deploy for development:
When you cloned project for the first time and want to start developing 
(or just play around) you have to do the following actions 
to deploy the project:

```
# configure virtual environment
python3 -m venv .venv

# activate virtual environment
source .venv/bin/activate

# install required packages
pip install -r requirements.txt

# run database migrations
./cli db upgrade

# install npm-packages
npm install

# build frontend
npm run build

# or run devServer
npm run dev
```

Or you can simply use command `make init` to do steps described above (except those related to database).
Also the command `make clean` can be used for cleaning development environment.
And you can combine these commands like this `make clean init` to recreate the environment.
Just run `make` to see little help with all available commands.


### CLI-commands

There are available some cli-commands to interact with.
For example, you can run server for development like this:

```
./cli run --host=0.0.0.0 --port=8000
```

This command will run server provided by Flask on port `8000`
and the application will be available by address `http://192.168.1.2:8000`
if your host machine has ip address `192.168.1.2`. **But don't use this server
in production!**

NOTE: before using `./cli` directly, you should make it executable (`chmod +x ./cli`).
Otherwise use this way: `python ./cli`

Other CLI-commands are described below by groups.

#### CLI-commands related to testing

```
# run all tests with detailed information
./cli test:run

# run all tests quietly
./cli test:run -q

# run only modular tests
./cli test:run --modular-only

# run only those tests which are testing web-pages
./cli test:run --web-only

# show code coverage
./cli test:coverage

# list all fixtures
./cli test:fixtures

# list all markers
./cli test:markers

# run code linting
./cli test:lint

# run only critical code linting
./cli test:lint --critical
```

#### CLI-commands for interacting with database

```
# initializing of migrations repository
./cli db init

# run all migrations that have not ran yet
./cli db upgrade

# show sql-code which is going to be executed
./cli db upgrade --sql

# migrate to specific mugration
./cli db upgrade <REVISION_HASH>

# create new migration-file with name
./cli db revision -m "Some new migration"

# revert to previous version
./cli db downgrade

# revert all migrations
./cli db downgrade base

# show list of migrations that already ran
# If flag `-i` specified - indicates what revision is current
./cli db history [-i]

# show detailed list of migrations
./cli db show
```

### Installed dependencies

Only following packages have been installed manually.
Other packages described in `requirements.txt` have been added as dependencies of these packages.

```
Flask
pytest
coverage
python-dotenv
flake8
Flask-SQLAlchemy
Flask-Migrate
PyMySql
```

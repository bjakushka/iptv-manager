# IPTV-Manager

[![Lint and test](https://github.com/bjakushka/iptv-manager/workflows/Lint%20and%20test/badge.svg?branch=main)](https://github.com/bjakushka/iptv-manager/actions?query=workflow%3A%22Lint+and+test%22)

Flask-based app for managing IPTV sources

Minimum required version of python: **3.8**
Minimum required version of node: **12.13.0**

### How to deploy for development:
When you cloned project for the first time and want to start developing 
(or just play around) you have to do the following actions 
to deploy the project:

```
# create the file `.env` with configuration (don't forget edit database URI)
# (you can use `.env.example` as a starting point)
cp .env.example .env

# initialize environment, database, execute tests and run the app
# NOTE: set option `IN_VIRTUALENV` in `.env` to `True` or execute `source ./venv/bin/activate` to enter virtual environment
make init && ./cli db upgrade && make test lint run

# you might want fill the database with some auto-generated data to play around
./cli seed --name=DemoDataSeeder

# now you can access the app by following address:
# http://<ip_address_of_your_server>:8000/
```

<details>
    <summary><strong>Full list of commands to deploy the project for development</strong></summary>
    
    # create the file `.env` with configuration
    # (you can use `.env.example` as a starting point)
    cp .env.example .env
    
    # configure the virtual environment
    python3 -m venv .venv
    
    # activate the virtual environment
    source .venv/bin/activate
    
    # install the required packages
    pip install -r requirements.txt
    
    # run database migrations
    ./cli db upgrade
    
    # install npm-packages
    npm install
    
    # build the frontend
    npm run build
    
    # make the cli-manager executable
    chmod +x ./cli
    
    # if you have not got real data yet you can seed the demo
    ./cli seed --name=DemoDataSeeder
    
    # run backend via development server
    ./cli run --host=0.0.0.0 --port=8000
    
    # now you can access the app by following address:
    # http://<ip_address_of_your_server>:8000/

</details>

During development you might want to run frontend in "hot"-mode:

```
# start npm in HMR-mode to re-build front on changes:
npm run dev
# and start server (use screen managers/another terminal tab/run it through IDEA)
make run
```


### Shortcuts

The project have Makefile with shortcuts to execute some routine and everyday commands.
Here is the list of these commands with short description:

```
# creates .venv, installs backend & frontend dependencies and does other initialization
make init

# removes .venv, logs, node_modules, pycache and other files
make clean 

# executes basic (critial) code linging and run tests
make test

# executes full code linting
make lint

# runs the development server
make run

# sometimes there is handy to execute some commands together:
# - re-deploy the project: `make clean init`
# - run all checks: `make lint test`
# also you can alway run `make all` to see all available shortcuts
```



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

<details>
    <summary><strong>CLI-commands related to testing</strong></summary>

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

</details>

<details>
    <summary><strong>CLI-commands for interacting with database</strong></summary>

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

</details>

<details>
    <summary><strong>CLI-commands for testing&linting</strong></summary>

    # run all tests
    ./cli test:run
    
    # run modular tests only
    ./cli test:run --modular-only
    
    # run tests with coverage
    ./cli test:run --cov
    
    # also you can combine different options
    ./cli test:run -modular-only --cov
    
    # start code linting (all)
    ./cli test:lint
    
    # start code linting (only critical)
    ./cli test:lint --critical
    
    # you can also run coverage like this
    ./cli test:coverage
    
    # display all available fixtures
    ./cli test:fixtures
    
    # list all markers for tests
    ./cli test:markers
    

</details>

<details>
    <summary><strong>How to play around with shell</strong></summary>

    ./cli shell
    >>> import app
    >>> channel_1 = app.models.Channel(name='First Channel')
    >>> channel_1
    <Channel #[NONE]>
    >>> app.db.session.add(channel_1)
    >>> app.db.session.commit()
    >>> channel_1
    <Channel #1>
    >>>
    >>> channel_2 = app.models.Channel.query.filter_by(id=1).first()
    >>> channel_2
    <Channel #1>
    >>> channel_2.name = 'Channel 2 (edited)'
    >>> app.db.session.add(channel_2)
    >>> app.db.session.commit()

</details>


### Project dependencies

Only following packages have been installed manually.
Other packages described in `requirements.txt` have been added as dependencies of these packages.

```
Flask
pytest
pytest-cov
coverage
python-dotenv
flake8
Flask-SQLAlchemy
Flask-Migrate
PyMySql
Flask-Restful
```

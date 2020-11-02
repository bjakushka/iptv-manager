# IPTV-Manager
Flask-based app for managing IPTV sources

Minimum required version of python: 3.8

### How to deploy for development:
When you cloned project for the first time and want to start developing (or just play around) you have to do the following actions to deploy the project:

```
# configure virtual environment
python3 -m venv .venv

# activate virtual environment
source .venv/bin/activate

# install required packages
pip install -r requirements.txt

# run database migrations
./cli db upgrade

```
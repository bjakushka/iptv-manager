import dotenv
import flask
import os
from distutils import util


class Loader:
    def __init__(self, env_file: str = '.env'):
        """Initialize configuration loader

        :param string env_file: Path to custom file with configuration variables
        """
        self.env_file = env_file
        self.config = self.load_application_config()

    def get_config(self) -> flask.Config:
        """Returns loaded instance of configuration."""

        return self.config

    def load_application_config(self) -> flask.Config:
        """Loads configuration for the application

        :rtype: flask.Config
        """
        config = self.load_default_config()

        # accept only keys which are defined in DefaultConfiguration
        accepted_keys = list(config.keys())

        # rewrite keys from default config by values from `.env`-file
        config.update(self.load_config_from_dotenv(self.env_file, accepted_keys=accepted_keys))

        # redefine keys by values taken from os environment
        config.update(self.load_config_from_env(accepted_keys=accepted_keys))

        return config

    @classmethod
    def load_config_from_dotenv(cls, env_file: str, accepted_keys: list = None) -> flask.Config:
        """Loads configuration variables from `.env`-file (or similar)

        If param `accepted_keys` is not instance of `list` - ALL keys will be accepted.

        :param string env_file: Path to custom file with configuration variables
        :param list of string accepted_keys: List of keys which can be accepted
        :rtype: flask.Config
        """
        config = flask.Config(os.path.dirname(__file__))
        all_keys_accepted = not isinstance(accepted_keys, list)
        for key, value in dotenv.dotenv_values(env_file).items():
            if key.isupper() and (all_keys_accepted or key in accepted_keys):
                config[key] = cls.parse_string_value(value)
        return config

    @classmethod
    def load_config_from_env(cls, accepted_keys: list = None) -> flask.Config:
        """Loads configuration from system's environment

        If param `accepted_keys` is not instance of `list` - NO keys will be accepted.

        :param list accepted_keys: List of keys which can be accepted
        :rtype: flask.Config
        """
        if not isinstance(accepted_keys, list):
            accepted_keys = []

        config = flask.Config(os.path.dirname(__file__))
        for key in accepted_keys:
            if key in os.environ:
                config[key] = cls.parse_string_value(os.environ[key])
        return config

    @staticmethod
    def load_default_config() -> flask.Config:
        """Loads configuration with default values

        :rtype: flask.Config
        """
        config = flask.Config(os.path.dirname(__file__))
        config.from_object(DefaultConfiguration)
        return config

    @staticmethod
    def parse_string_value(value: str) -> [str, bool]:
        """Parses value of the setting from .env-file

        If value in `value` can be boolean - parses it and returns boolean.
        In other case returns `value` itself.

        :param string value: Value to parse.
        :rtype: string|bool
        """
        try:
            return bool(util.strtobool(value))
        except ValueError:
            return value


class DefaultConfiguration:
    """Defines default configuration for the application"""
    # common
    #
    FLASK_ENV = 'production'
    FLASK_DEBUG = False
    TESTING = False
    SECRET_KEY = None
    JSON_SORT_KEYS = True
    JSON_PRETTYPRINT_REGULAR = False
    IN_VIRTUALENV = False

    # database
    #
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = True

import flask
import os
import pytest

from app.config import Loader as ConfigLoader


#
# test the class itself
#

def test_config_loader_empty_file_no_env(tmp_path):
    """Loading application configuration with no `.env`-file or environment variables"""
    env_file = tmp_path / ".env"
    env_file.write_text('')

    test_cases = [
        ('FLASK_ENV', 'production'),
        ('FLASK_DEBUG', False),
        ('TESTING', False),
        ('SECRET_KEY', None),
        ('JSON_SORT_KEYS', True),
        ('JSON_PRETTYPRINT_REGULAR', False),
        ('IN_VIRTUALENV', False),
    ]

    config = ConfigLoader(str(env_file)).get_config()
    assert isinstance(config, flask.Config), ''
    assert len(config) == 7, 'Unexpected amount of configuration-keys'
    for case in test_cases:
        assert config.get(case[0]) == case[1], \
            'Default value of `{}` should be `{}`'.format(case[0], case[1])


def test_config_loader_non_empty_file_no_env(tmp_path):
    """Load application configuration with existing `.env`-file"""
    env_file = tmp_path / ".env"
    env_file.write_text('SECRET_KEY = "super_secret_key"\nNOT_ACCEPTED_KEY = True')

    config = ConfigLoader(str(env_file)).get_config()
    assert config.get('SECRET_KEY') == "super_secret_key", 'Keys from `.env` must take precedence over defaults'
    assert 'NOT_ACCEPTED_KEY' not in config, 'Not allowed keys should not be added'


def test_config_loader_non_empty_file_with_env(tmp_path):
    """Load application configuration with existing `.env`-file and environment variables"""
    env_file = tmp_path / '.env'
    env_file.write_text('SECRET_KEY = "super_secret_key\nNOT_ACCEPTED_KEY = True')

    # modify environment variables
    old_value = getattr(os.environ, 'SECRET_KEY', None)
    os.environ['SECRET_KEY'] = 'super_secret_key_from_env'
    os.environ['NOT_ACCEPTED_KEY'] = 'True'

    config = ConfigLoader(str(env_file)).get_config()

    # restore state of environment variables
    if not old_value:
        del os.environ['SECRET_KEY']
    else:
        os.environ['SECRET_KEY'] = old_value
    del os.environ['NOT_ACCEPTED_KEY']

    assert config.get(
        'SECRET_KEY') == 'super_secret_key_from_env', 'Keys from environment must take precedence over defaults and values from `.env`-file'
    assert 'NOT_ACCEPTED_KEY' not in config, 'Not allowed keys should not be added'


#
# test the class's methods separately
#

#
# loading from .env-file

def test_load_config_from_dotenv_empty_file(tmp_path):
    """Checks that configuration loading properly works with empty `.env` files"""
    env_file = tmp_path / ".env"
    env_file.write_text('')

    config = ConfigLoader.load_config_from_dotenv(str(env_file))
    assert len(config) == 0, 'Empty `.env` should return empty `Config`-instance'


def test_load_config_from_dotenv_non_empty_file(tmp_path):
    """Loading configuration from `.env`-file"""
    env_file = tmp_path / ".env"
    env_file.write_text('VALID = true\ntruly_invalid = true\nInVaLiD = true')

    config = ConfigLoader.load_config_from_dotenv(str(env_file))
    assert len(config) == 1, 'Resulting `Config`-instance should contain only one key-value pair'
    assert 'VALID' in config, '`VALID` key should be in resulting config'
    assert 'InVaLiD' not in config and 'truly_invalid' not in config, 'Other invalid keys should not be in resulting config'


def test_load_config_from_dotenv_non_empty_file_all_keys_accepted(tmp_path):
    """Loading configuration from `.env`-file when all keys are accepted"""
    env_file = tmp_path / ".env"
    env_file.write_text('VALID = true\ntruly_invalid = true\nInVaLiD = true')

    config = ConfigLoader.load_config_from_dotenv(str(env_file), accepted_keys=None)
    assert len(config) == 1, 'Resulting `Config`-instance should contain only one key-value pair'
    assert 'VALID' in config, '`VALID` key should be in resulting config'
    assert 'InVaLiD' not in config and 'truly_invalid' not in config, 'Other invalid keys should not be in resulting config'


def test_load_config_from_dotenv_non_empty_file_no_keys_accepted(tmp_path):
    """Load configuration from `.env`-file but not accept any keys"""
    env_file = tmp_path / ".env"
    env_file.write_text('VALID = true\nNOT_ACCEPTED = true\nInVaLiD = true')

    config = ConfigLoader.load_config_from_dotenv(str(env_file), accepted_keys=[])
    assert len(config) == 0, 'Resulting `Config`-instance should be empty - there are no accepted keys'


def test_load_config_from_dotenv_non_empty_file_some_keys_accepted(tmp_path):
    """Load configuration from `.env`-file but accept some keys"""
    env_file = tmp_path / ".env"
    env_file.write_text('VALID = true\nNOT_ACCEPTED = true')

    config = ConfigLoader.load_config_from_dotenv(str(env_file), accepted_keys=['VALID'])
    assert len(config) == 1, 'Resulting `Config`-instance should contain only one key-value pair'
    assert 'VALID' in config, 'Accepted keys must be added'
    assert 'NOT_ACCEPTED' not in config, 'Keys other than accepted must not be added'


#
# loading from env

def test_load_config_from_env(tmp_path):
    """Tests properly work of loading configuration from environment variables"""
    # modify environment variables
    old_value = getattr(os.environ, 'NOT_ACCEPTED_KEY', None)
    os.environ['NOT_ACCEPTED_KEY'] = "-42"
    os.environ['NOT_ACCEPTED_KEY_ANOTHER_ONE'] = "True"

    config = ConfigLoader.load_config_from_env()

    # restore state of environment variables
    if not old_value:
        del os.environ['NOT_ACCEPTED_KEY']
    else:
        os.environ['NOT_ACCEPTED_KEY'] = old_value
    del os.environ['NOT_ACCEPTED_KEY_ANOTHER_ONE']

    assert len(config) == 0, 'Resulting `Config`-instance should be empty - there are no accepted keys'


def test_load_config_from_env_no_keys_accepted(tmp_path):
    """Tests properly work of loading configuration from environment variables when no keys are accepting"""
    # modify environment variables
    old_value = getattr(os.environ, 'NOT_ACCEPTED_KEY', None)
    os.environ['NOT_ACCEPTED_KEY'] = "-42"
    os.environ['NOT_ACCEPTED_KEY_ANOTHER_ONE'] = "True"

    config = ConfigLoader.load_config_from_env(accepted_keys=[])

    # restore state of environment variables
    if not old_value:
        del os.environ['NOT_ACCEPTED_KEY']
    else:
        os.environ['NOT_ACCEPTED_KEY'] = old_value
    del os.environ['NOT_ACCEPTED_KEY_ANOTHER_ONE']

    assert len(config) == 0, 'Resulting `Config`-instance should be empty - there are no accepted keys'


def test_load_config_from_env_some_keys_accepted(tmp_path):
    """Tests properly work of loading configuration from environment variables when some keys are accepting"""
    # modify environment variables
    old_value = getattr(os.environ, 'ACCEPTED_KEY', None)
    os.environ['ACCEPTED_KEY'] = "-42"
    os.environ['NOT_ACCEPTED_KEY'] = "True"

    config = ConfigLoader.load_config_from_env(accepted_keys=['ACCEPTED_KEY'])

    # restore state of environment variables
    if not old_value:
        del os.environ['ACCEPTED_KEY']
    else:
        os.environ['ACCEPTED_KEY'] = old_value
    del os.environ['NOT_ACCEPTED_KEY']

    assert len(config) == 1, 'Resulting `Config`-instance should contain only one key-value pair'
    assert 'ACCEPTED_KEY' in config, 'Accepted keys must be added'
    assert 'NOT_ACCEPTED_KEY' not in config, 'Keys other than accepted must not be added'


#
# loading default config


def test_load_default_config():
    """Loading of configuration by default"""
    config = ConfigLoader.load_default_config()
    assert len(config) == 7, 'Not expected amount of config-keys'


# parsing

def test_parse_string_value_valid_values():
    """Tests properly work of method, which parse values from `.env`-files, with valid values"""
    test_cases = [
        ('TRUE', True),
        ('False', False),
        ('0', False),
        ('1', True),
        ('Just a string', 'Just a string'),
        ('5', '5'),
        ('', ''),
    ]

    for case in test_cases:
        assert ConfigLoader.parse_string_value(case[0]) == case[1], \
            '`{}` should be treated as `{}`'.format(case[0], case[1])


def test_parse_string_value_invalid_values():
    """Tests method with invalid values"""
    with pytest.raises(AttributeError):
        # noinspection PyTypeChecker
        ConfigLoader.parse_string_value(1)

import pytest
from . import helpers


@pytest.fixture(scope='session')
def app_instance():
    """Returns instance of application for further testing.

    :rtype: flask.Flask
    """
    from app import app

    helpers.configure_application_for_testing(app)

    yield app


@pytest.fixture
def prepare_context(app_instance):
    """Pushes application context.

    :param flask.Flask app_instance:
    :rtype: flask.ctx.AppContext
    """

    context = app_instance.app_context()
    context.push()

    yield context

    context.pop()


@pytest.fixture
def client(app_instance, prepare_context):
    """Prepares Werkzeug Client for testing application.

    :param flask.Flask app_instance:
    :param flask.ctx.AppContext prepare_context:
    :rtype: flask.testing.FlaskClient
    """
    client = app_instance.test_client()

    yield client

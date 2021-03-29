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


@pytest.fixture(scope='session')
def models():
    """Returns whole module with all defined models"""
    from app import models
    return models


@pytest.fixture(scope='function')
def base_model(models):
    """Returns instance of BaseModel for testing purposes

    :rtype: app.models.BaseModel
    """
    return models.BaseModel()


@pytest.fixture(scope='session')
def almost_base_model_class(models):
    """Returns class which is "almost" like BaseClass

    Defines minimally modified sub-class of BaseModel.
    This class created for test some basic methods defined in BaseModel.

    :rtype: type of app.models.BaseModel
    """
    from app import db

    class AlmostBaseModel(models.BaseModel):
        __tablename__ = 'not_existing_table'

        # own properties
        id = db.Column(db.Integer, primary_key=True)

    return AlmostBaseModel


@pytest.fixture(scope='function')
def almost_base_model(almost_base_model_class):
    """Returns instance of AlmostBaseModel

    :param almost_base_model_class:
    :rtype: app.models.BaseModel
    """
    return almost_base_model_class(id=42)

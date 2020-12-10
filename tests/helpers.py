def configure_application_for_testing(app):
    """Configures application for running testing in special environment.

    :param flask.Flask app:
    """
    app.config['TESTING'] = True

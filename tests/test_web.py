import pytest

pytestmark = [pytest.mark.webtest]


def test_index_availability(client):
    """Index page must be present and HTTP Status Code have to be `200`"""
    response = client.get('/')
    assert response.status_code == 200


def test_not_existing_url(client):
    """Not existing URL must return `200` and display index page"""
    response = client.get('/not-exists')
    assert response.status_code == 200

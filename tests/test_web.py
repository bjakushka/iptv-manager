import pytest

pytestmark = [pytest.mark.webtest]


def test_index_availability(client):
    """Index page must be present and HTTP Status Code have to be `200`"""
    response = client.get('/')
    assert response.status_code == 200


def test_not_existing_url(client):
    """Not existing endpoint must return HTTP Status Code `404`"""
    response = client.get('/not-exists')
    assert response.status_code == 404

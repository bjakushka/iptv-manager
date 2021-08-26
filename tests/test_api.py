import pytest

pytestmark = [pytest.mark.webtest]


def test_ping(client):
    """Testing api-endpoint have to return `pong` when request"""
    response = client.get('/api/ping')
    assert response.status_code == 200

    data = response.json.get('data')
    assert dict.get(data, 'answer', None) == 'pong'


def test_not_existing_url(client):
    """Request of not existing api-endpoint have to return 404`
    """
    response = client.get('/api/not-existing')
    assert response.status_code == 404

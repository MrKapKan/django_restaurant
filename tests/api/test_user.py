import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

client = APIClient()


@pytest.mark.django_db
def test_unauthorized_access_dishes():
    response = client.post('/api/v1/dishes/')

    assert response.status_code == 401


@pytest.mark.django_db
def test_restaurant_create():
    payload = {"title": "McDonalds",
               "address": "Main street"}
    response = client.post('/api/v1/restaurant/', payload)
    data = response.data

    assert response.status_code == 201
    assert data == {
        "id": 1,
        "title": "McDonalds",
        "address": "Main street"
    }


@pytest.mark.django_db
def test_get_token():
    User = get_user_model()
    User.objects.create_superuser('root', 'admin@myproject.com', 'root')
    payload = {"username": "root",
               "password": "root"}
    response = client.post('/api/v1/token/', payload)
    data = response.data

    assert response.status_code == 200
    assert "refresh" in data
    assert "access" in data




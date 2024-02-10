import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status
from backend_api.models import User, Review, Airport

@pytest.mark.django_db
def test_user_details_post():
    client = Client()
    user_data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }
    response = client.post(reverse('userdetails'), data=user_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1
    assert User.objects.get().username == 'testuser'

@pytest.mark.django_db
def test_user_details_get():
    User.objects.create(username='testuser', email='testuser@example.com', password='testpassword')
    client = Client()
    response = client.get(reverse('userdetails'))
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]['username'] == 'testuser'

@pytest.mark.django_db
def test_review_list_get():
    user = User.objects.create(username='testuser', email='testuser@example.com', password='testpassword')
    airport = Airport.objects.create(name='Test Airport')
    Review.objects.create(user=user, airport=airport, comment='This is a test review.', category='General')
    client = Client()
    response = client.get(reverse('reviewlist'))
    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]['comment'] == 'This is a test review.'
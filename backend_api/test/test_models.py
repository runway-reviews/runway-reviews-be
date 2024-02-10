import pytest
from backend_api.models import User, Airport, Review
from django.test import TestCase
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create(
        username='testuser',
        email='testuser@example.com',
        password='testpassword'
    )
    assert user.username == 'testuser'
    assert user.email == 'testuser@example.com'
    assert user.password == 'testpassword'

@pytest.mark.django_db
def test_airport_creation():
    airport = Airport.objects.create(
        name='Test Airport'
    )
    assert airport.name == 'Test Airport'

@pytest.mark.django_db
def test_review_creation():
    user = User.objects.create(
        username='testuser',
        email='testuser@example.com',
        password='testpassword'
    )
    airport = Airport.objects.create(
        name='Test Airport'
    )
    review = Review.objects.create(
        user=user,
        airport=airport,
        comment='This is a test review.',
        category='General'
    )
    assert review.user == user
    assert review.airport == airport
    assert review.comment == 'This is a test review.'
    assert review.category == 'General'
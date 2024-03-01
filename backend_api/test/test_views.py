import pytest
from django.test import TestCase
from backend_api.models import Review, Airport, User
from django.core.exceptions import ValidationError

@pytest.mark.django_db
class TestReviewView:
    def test_review_creation(self):
        user = User.objects.create(username='testuser', password='12345')
        airport = Airport.objects.create(name='Test Airport')
        review = Review.objects.create(
            user=user,
            airport=airport,
            category='General',
            comment='This is a test review comment.'
        )
        assert review.user == user, "The user should be saved and retrieved correctly."
        assert review.airport == airport, "The airport should be saved and retrieved correctly."
        assert review.category == 'General', "The category should be saved and retrieved correctly."
        assert review.comment == 'This is a test review comment.', "The comment should be saved and retrieved correctly."
        assert Review.objects.count() == 1, "There should be one review in the database."
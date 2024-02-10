import pytest
from django.test import TestCase
from backend_api.models import Review, Airport, User
from django.core.exceptions import ValidationError


@pytest.mark.django_db
class TestReviewModel:
    @pytest.mark.parametrize("tag, expected", Review.CATEGORY_TAGS)
    def test_category_tag_creation(self, tag, expected):
        review = Review.objects.create(category=tag, comment="Sample review comment.")
        saved_review = Review.objects.get(id=review.id)
        assert saved_review.category == tag, f"Category tag '{tag}' should be saved and retrieved correctly."
        assert saved_review.comment == "Sample review comment.", "The comment should be saved and retrieved correctly."

    def test_invalid_category_tag(self):
      review = Review(category='invalid_tag', comment="Sample comment")
      with pytest.raises(ValidationError):
        review.full_clean()

    def test_review_str(self):
        test_user = User.objects.create(username='testuser', password='12345')
        test_airport = Airport.objects.create(name='Test Airport')

        review_comment = "This is a sample review comment."
        review = Review.objects.create(
            user=test_user,
            airport=test_airport,
            category='General',  
            comment=review_comment
        )

        assert str(review) == review_comment, "The __str__ method should return the review comment."


  #I don't know why this isn't working
    # def test_comment_length_validation(self):
    #   long_comment = 'a' * 155
    #   review = Reviews(category='general', comment=long_comment)
    #   with pytest.raises(ValidationError):
    #     review.full_clean()


@pytest.fixture
def name():
    return 'Test Airport Name'
@pytest.mark.django_db
class TestAirportModel:
  def test_airport_name_creation(self, name):
    airport = Airport.objects.create(name=name)
    saved_airport = Airport.objects.get(id=airport.id)
    assert saved_airport.name == name, f"Category tag '{name}' should be saved and retrieved correctly."
  def test_user_str(self, username):
    airport = Airport.objects.create(name='test airport')
    assert str(airport) == 'test airport'

@pytest.fixture
def username():
    return 'Test User Name'
@pytest.fixture
def email():
    return 'Test User Email'
@pytest.fixture
def password():
    return 'TestPassword'
@pytest.mark.django_db
class TestUserModel:
  def test_user_name_creation(self, username):
    user = User.objects.create(username=username)
    saved_user = User.objects.get(id=user.id)
    assert user.username == username, f"Category tag '{username}' should be saved and retrieved correctly."
  def test_user_email_creation(self, email):
    user = User.objects.create(email=email)
    saved_user = User.objects.get(id=user.id)
    assert user.email == email, f"Category tag '{email}' should be saved and retrieved correctly."
  def test_user_password_creation(self, password):
    user = User.objects.create(password=password)
    saved_user = User.objects.get(id=user.id)
    assert user.password == password, f"Category tag '{password}' should be saved and retrieved correctly."
  def test_user_str(self, username):
    user = User.objects.create(username='testuser', email='test@example.com', password='12345')
    assert str(user) == 'testuser'


# Create your tests here.

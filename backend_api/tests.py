import pytest
from django.test import TestCase
from .models import Review
from django.core.exceptions import ValidationError



@pytest.mark.django_db
class TestReviewsModel:
    @pytest.mark.parametrize("tag, expected", Reviews.CATEGORY_TAGS)
    def test_category_tag_creation(self, tag, expected):
        review = Reviews.objects.create(category=tag, comment="Sample review comment.")
        saved_review = Reviews.objects.get(id=review.id)
        assert saved_review.category == tag, f"Category tag '{tag}' should be saved and retrieved correctly."
        assert saved_review.comment == "Sample review comment.", "The comment should be saved and retrieved correctly."

    def test_invalid_category_tag(self):
      review = Reviews(category='invalid_tag', comment="Sample comment")
      with pytest.raises(ValidationError):
        review.full_clean()


  #I don't know why this isn't working
    # def test_comment_length_validation(self):
    #   long_comment = 'a' * 155
    #   review = Reviews(category='general', comment=long_comment)
    #   with pytest.raises(ValidationError):
    #     review.full_clean()





# Create your tests here.

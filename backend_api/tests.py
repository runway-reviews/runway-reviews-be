# import pytest
# from django.test import TestCase
# from .models import Review
# from django.core.exceptions import ValidationError



# @pytest.mark.django_db
# class TestReviewModel:
#     @pytest.mark.parametrize("tag, expected", Review.CATEGORY_TAGS)
#     def test_category_tag_creation(self, tag, expected):
#         review = Review.objects.create(category=tag, comment="Sample review comment.")
#         saved_review = Review.objects.get(id=review.id)
#         assert saved_review.category == tag, f"Category tag '{tag}' should be saved and retrieved correctly."
#         assert saved_review.comment == "Sample review comment.", "The comment should be saved and retrieved correctly."

#     def test_invalid_category_tag(self):
#       review = Review(category='invalid_tag', comment="Sample comment")
#       with pytest.raises(ValidationError):
#         review.full_clean()


  #I don't know why this isn't working
    # def test_comment_length_validation(self):
    #   long_comment = 'a' * 155
    #   review = Reviews(category='general', comment=long_comment)
    #   with pytest.raises(ValidationError):
    #     review.full_clean()





# Create your tests here.

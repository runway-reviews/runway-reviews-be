from django.test import TestCase
from rest_framework.serializers import ValidationError
from serializers import ReviewSerializer
from backend_api.models import Review, User, Airport

class ReviewSerializerTest(TestCase):
  def test_review_serializer(self):
    data = {
      "id": "1",
      "user_id": "1",
      "airport_id": "1",
      "category": "security",
      "comment": "TSA seemed a little TOO handsy for my liking."
    }

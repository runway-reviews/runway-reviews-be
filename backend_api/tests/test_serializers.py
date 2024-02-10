from django.test import TestCase
from rest_framework.serializers import ValidationError
from serializers import UserSerializer, ReviewSerializer, AirportSerializer
from backend_api.models import Review, User, Airport


class UserSerializerTest(TestCase):
  def test_user_serializer(self):
    data = {
      "id": "1",
      "username": "snickers1",
      "password": "password"
    }
    serializer = UserSerializer(data=data)
    self.assertTrue(serializer.is_valid())

    self.assertEqual(serializer.errors, {})

class UserSerializerInvalid(TestCase):
  def test_user_serializer_invalid(self):
    data = {
      "id": "1",
      "username": "snickers1"
    }
    serializer = UserSerializer(data=data)
    self.assertTrue(serializer.is_valid())

    self.assertNotEqual(serializer.errors, {})



class ReviewSerializerTest(TestCase):
  def test_review_serializer(self):
    data = {
      "id": "1",
      "user_id": "1",
      "airport_id": "1",
      "category": "security",
      "comment": "TSA seemed a little TOO handsy for my liking."
    }
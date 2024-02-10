from django.test import TestCase
from rest_framework.serializers import ValidationError
from serializers import UserSerializer

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
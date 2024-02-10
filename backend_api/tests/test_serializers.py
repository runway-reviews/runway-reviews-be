# from django.test import TestCase
# from rest_framework import serializers 
# from serializers import UserSerializer, ReviewSerializer, AirportSerializer
# from backend_api.models import Review, User, Airport


# class UserSerializerTest(TestCase):
#   def test_user_serializer(self):
#     data = {
#       "username": "snickers1",
#       "email": "cutiepatottie@gmail.com",
#       "password": "password"
#     }
#     serializer = UserSerializer(data=data)
#     self.assertTrue(serializer.is_valid())

#     self.assertEqual(serializer.errors, {})

# class UserSerializerInvalid(TestCase):
#   def test_user_serializer_invalid(self):
#     data = {
#       "id": "1",
#       "username": "snickers1"
#     }
#     serializer = UserSerializer(data=data)
#     self.assertTrue(serializer.is_valid())

#     self.assertNotEqual(serializer.errors, {})



# class ReviewSerializerTest(TestCase):
#   def test_review_serializer(self):
#     data = {
#       "id": "1",
#       "user_id": "1",
#       "airport_id": "1",
#       "category": "security",
#       "comment": "TSA seemed a little TOO handsy for my liking."
#     }

# class UserSerializerTest(TestCase):
#     def setUp(self):
#         self.user_data = {
#             'username': 'testuser',
#             'email': 'testuser@example.com',
#             'password': 'testpassword'
#         }
#         self.user = User.objects.create(**self.user_data)

#     def test_user_serializer(self):
#         serializer = UserSerializer(instance=self.user)
#         data = serializer.data

#         self.assertEqual(data['id'], str(self.user.pk))
#         self.assertEqual(data['type'], 'user')
#         self.assertEqual(data['attributes']['username'], self.user_data['username'])
#         self.assertEqual(data['attributes']['email'], self.user_data['email'])

# class ReviewSerializerTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='testuser', email='testuser@example.com', password='testpassword')
#         self.airport = Airport.objects.create(name='Test Airport')
#         self.review_data = {
#             'user': self.user,
#             'airport': self.airport,
#             'comment': 'Test comment',
#             'category': 'Test category'
#         }
#         self.review = Review.objects.create(**self.review_data)

#     def test_review_serializer(self):
#         serializer = ReviewSerializer(instance=self.review)
#         data = serializer.data

#         self.assertEqual(data['id'], self.review.id)
#         self.assertEqual(data['type'], 'review')
#         self.assertEqual(data['attributes']['comment'], self.review.comment)
#         self.assertEqual(data['attributes']['category'], self.review.category)
#         self.assertEqual(data['relationships']['user']['data']['id'], str(self.user.pk))

# class AirportSerializerTest(TestCase):
#     def setUp(self):
#         self.airport_data = {
#             'name': 'Test Airport'
#         }
#         self.airport = Airport.objects.create(**self.airport_data)

#     def test_airport_serializer(self):
#         serializer = AirportSerializer(instance=self.airport)
#         data = serializer.data

#         self.assertEqual(data['id'], self.airport.id)
#         self.assertEqual(data['attributes']['name'], self.airport_data['name'])

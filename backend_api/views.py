import json
import requests
from rest_framework import status 
from rest_framework.views import APIView  
from rest_framework.response import Response
from backend_api.models import User, Review, Airport
from backend_api.serializers import UserSerializer, ReviewSerializer, AirportSerializer
from django.http import JsonResponse
from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import get_object_or_404


# Review actions  
def get_airports(request):
  url = "https://api.api-ninjas.com/v1/airports?country=us"
  headers = { 
    "X-Api-Key": "wBYJMUcWGyoBJKsUT34CEg==Yd6H5zc6HAjbeSHC"
  }
  # airports = Airport.objects.all()
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
      data = response.json()
      # serializer = AirportSerializer(airports, many=True)
      return response.json()
  else:
      return JsonResponse({"error": "Failed to fetch data"}, status=500)
  
def airports(request):
    updated_airports = []
    try: 
      airports_data = get_airports(request)
      for airport_data in airports_data:
        airport, created = Airport.objects.update_or_create(
          name=airport_data['name'],
        )
        updated_airports.append(airport)
        if created:
            print(f"Created new airport: {airport.name}")
        else:
            print(f"Updated existing airport: {airport.name}")
      serializer = AirportSerializer(updated_airports, many=True)
      return JsonResponse(serializer.data, safe=False, status=200)
    except IntegrityError as e:
        print(f"Database error occurred: {e}")
        return JsonResponse({"error": str(e)}, status=500)
    except Exception as e:
        print(f"An error occurred: {e}")
        return JsonResponse({"error": str(e)}, status=500)

class UserDetails(APIView):
  def post(self, request):
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
  def get(self, request, format=None):
      users = User.objects.all()
      serializer = UserSerializer(users, many=True)
      return Response(serializer.data)

class ReviewList(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

      
class ReviewDetails(APIView):
    def get_user(self, user_id):
      try: 
          return User.objects.get(pk=user_id)
      except User.DoesNotExist: 
          raise Http404("User does not exist")

    def get_review(self, review_id):
      try: 
          return Review.objects.get(pk=review_id)
      except: 
          return Response({
            'error': 'Review does not exist' 
            }, status=status.HTTP_404_NOT_FOUND)
      
    def get_airport(self, airport_id):
      try: 
          return Airport.objects.get(pk=airport_id)
      except Airport.DoesNotExist: 
          raise Http404("Airport does not exist")

    def get(self, request, review_id):
        review = self.get_review(review_id)
        if isinstance(review, Response):
            return review
        serializer = ReviewSerializer(review)
        return Response(serializer.data) 

    def post(self, request, user_id, format=None):
      user = self.get_user(user_id)
      if isinstance(user, Http404):
          return Response({'error': str(user)}, status=status.HTTP_404_NOT_FOUND)

      airport_id = request.data.get('airport_id')
      if not airport_id:
          return Response({"error": "airport_id is required"}, status=status.HTTP_400_BAD_REQUEST)

      airport = self.get_airport(airport_id)
      if isinstance(airport, Http404):
          return Response({'error': str(airport)}, status=status.HTTP_404_NOT_FOUND)

      serializer = ReviewSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save(user=user, airport=airport)
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id, review_id, format=None):
      review = get_object_or_404(Review, pk=review_id)
      review.delete()
      return Response({'message': 'Review deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
     


      
    

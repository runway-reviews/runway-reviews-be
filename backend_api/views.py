# from django.shortcuts import render, HttpResponse
import requests
import json
from rest_framework.views import APIView 
from backend_api.models import User, Review, Airport   
from backend_api.serializers import UserSerializer, ReviewSerializer, AirportSerializer 
from rest_framework.response import Response
from rest_framework import status 
from django.http import JsonResponse
from django.db import IntegrityError

# User actions 
class UserDetails(APIView):

  # create users
  def post(self, request):
      serializer = UserSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Review actions  
class ReviewDetails(APIView):

  # set_user
  def get_user(request, user_id):
    try: 
        return User.objects.get(pk=user_id)
    except: 
        return Response({
          'error': 'User does not exist' 
          }, status=status.HTTP_404_NOT_FOUND)
  # set_user
  def get_user(request, user_id):
    try: 
        return User.objects.get(pk=user_id)
    except: 
        return Response({
          'error': 'User does not exist' 
          }, status=status.HTTP_404_NOT_FOUND)

  # set_review
  def get_review(request, review_id):
    try: 
        return Review.objects.get(pk=review_id)
    except: 
        return Response({
          'error': 'Review does not exist' 
          }, status=status.HTTP_404_NOT_FOUND)

  # get review
  def get(self, request, review_id, user_id):
      review = self.get_review(review_id)
      user = self.get_user(user_id)
      serializer = ReviewSerializer(review, user) # integrating the airport id into the serializer here 
      return Response(serializer.data) 

  def post(self, request, review_id, user_id):
      review = self.get_review(review_id)
      user = self.get_user(user_id)
      serializer = ReviewSerializer(data=request.data)
      
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
  
def airport_list(request):
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

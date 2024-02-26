from django.db import IntegrityError
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from backend_api.models import *
from backend_api.serializers import UserSerializer, ReviewSerializer, AirportSerializer
# from django.conf import settings
# from rest_framework import generics
from bs4 import BeautifulSoup
import pdb

# SIMPLE_API_KEY = settings.SIMPLE_API_KEY
def get_airports(request):

    url = "https://www.stratosjets.com/blog/busiest-us-airports/"
    response = requests.get(url)

    # Parse the content of the response with Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Now you can use the 'soup' object to find elements in the page
    post_content_divs = soup.find_all('div', class_='post-content entry-content')

    # Initialize an empty list
    airport_list = []

    for div in post_content_divs:
        header = div.find('h2')
        if header and header.text.strip() == "What Are the Top 20 Busiest Airports in the United States?":
            ol_element = div.find('ol')
            if ol_element:
                li_elements = ol_element.find_all('li')
                for li in li_elements:
                    # Split the text on '–' and take the first part
                    airport_name = li.text.split('–')[0].strip()
                    # Append the airport name to the list
                    airport_list.append(airport_name)

    # Now 'airport_list' is a list of airport names
    print(airport_list)

def airports(request):

    airport_list = get_airports(request)

    if airport_list is None:
        return JsonResponse([], safe=False, status=200)

    updated_airports = []

    for airport_name in airport_list:
        airport, created = Airport.objects.update_or_create(
            name=airport_name,
        )
        updated_airports.append(airport)
        if created:
            print(f"Created new airport: {airport.name}")
        else:
            print(f"Updated existing airport: {airport.name}")

    serializer = AirportSerializer(updated_airports, many=True)
    return JsonResponse(serializer.data, safe=False, status=200)

# Review actions  
# def get_airports(request):
#   url = "https://api.api-ninjas.com/v1/airports?country=us"
#   headers = { 
#     "X-Api-Key": SIMPLE_API_KEY
#   }
#   response = requests.get(url, headers=headers)
#   if response.status_code == 200:
#       return response.json()
#   else:
#       return JsonResponse({"error": "Failed to fetch data"}, status=500)
  
  
# def airports(request):
#     updated_airports = []
#     try: 
#       airports_data = get_airports(request)
#       for airport_data in airports_data:
#         airport, created = Airport.objects.update_or_create(
#           name=airport_data['name'],
#         )
#         updated_airports.append(airport)
#         if created:
#             print(f"Created new airport: {airport.name}")
#         else:
#             print(f"Updated existing airport: {airport.name}")
#       serializer = AirportSerializer(updated_airports, many=True)
#       return JsonResponse(serializer.data, safe=False, status=200)
#     except IntegrityError as e:
#         print(f"Database error occurred: {e}")
#         return JsonResponse({"error": str(e)}, status=500)
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return JsonResponse({"error": str(e)}, status=500)

# class AirportList(generics.ListCreateAPIView):
#     queryset = Airport.objects.all()
#     serializer_class = AirportSerializer
    
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
        return get_object_or_404(User, pk=user_id)

    def get_review(self, review_id):
        return get_object_or_404(Review, pk=review_id)

    def get_airport(self, airport_id):
        return get_object_or_404(Airport, pk=airport_id)

    def get(self, request, review_id):
        review = self.get_review(review_id)
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
     


      
    

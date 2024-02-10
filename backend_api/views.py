from django.db import IntegrityError
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from backend_api.models import User, Review, Airport
from backend_api.serializers import UserSerializer, ReviewSerializer, AirportSerializer
from django.conf import settings

SIMPLE_API_KEY = settings.SIMPLE_API_KEY



# Review actions  
def get_airports(request):
    url = "https://api.api-ninjas.com/v1/airports?country=us"
    headers = {
        "X-Api-Key": SIMPLE_API_KEY
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        try:
            return response.json()
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            return {"error": "Failed to parse JSON response"}
    else:
        return {"error": "Failed to fetch data from the API", "status_code": response.status_code}

def airports(request):
    updated_airports = []
    try:
        airports_data = get_airports(request)
        
        # Check if airports_data is a list
        if not isinstance(airports_data, list):
            raise ValueError("Invalid data structure for airports_data")
        
        for airport_data in airports_data:
            # Ensure airport_data is a dictionary
            if not isinstance(airport_data, dict):
                raise ValueError("Invalid data structure for an airport entry")
            
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
    except ValueError as e:
        print(f"Value error occurred: {e}")
        return JsonResponse({"error": str(e)}, status=400)
    except TypeError as e:
        print(f"Type error occurred: {e}")
        return JsonResponse({"error": "Incorrect data type encountered"}, status=400)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return JsonResponse({"error": "An unexpected error occurred"}, status=500)

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
     


      
    

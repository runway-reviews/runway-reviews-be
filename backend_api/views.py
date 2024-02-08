from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView 
from backend_api.models import User 
from backend_api.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status 
from django.http import HttpResponse

def reviews(request):
  return HttpResponse("reviews")
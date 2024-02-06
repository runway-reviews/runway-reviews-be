from django.contrib import admin
from django.urls import path
from backend_api.views import UserCreate, ReviewCreate, AirportIndex, AirportReviewsIndex 

urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:pk>', BookDetail.as_view()) 
    
    path('users/', UserCreate.as_view())
]
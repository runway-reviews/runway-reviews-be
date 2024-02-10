from django.contrib import admin
from django.urls import path
from backend_api.views import UserDetails, ReviewDetails, ReviewList
from backend_api import views

urlpatterns = [
    path('user', UserDetails.as_view(), name='create_user'),
    path('user', UserDetails.as_view(), name='user_details'),
    path('user/<int:user_id>/review/', views.ReviewDetails.as_view(), name='create_review'),
    path('user/<int:user_id>/review/<int:review_id>', ReviewDetails.as_view(), name='review_details'),
    path('user/<int:user_id>/reviews/<int:review_id>', ReviewDetails.as_view(), name='delete_review'),
    path('reviews', ReviewList.as_view(), name='review-list'),
    path('get-airports/', views.get_airports, name='get_airports'),
    path('airports/', views.airports, name='airports'),

]
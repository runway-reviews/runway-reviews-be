from django.contrib import admin
from django.urls import path
from backend_api.views import UserDetails, ReviewDetails, airports
from backend_api import views

urlpatterns = [
    path('user', UserDetails.as_view()),
    path('user/<int:user_id>/review/', ReviewDetails.as_view(), name='create_review'),
    path('user/<int:user_id>/review/<int:review_id>', ReviewDetails.as_view(), name='review-details'),
    path('user/<int:user_id>/reviews/<int:review_id>', ReviewDetails.as_view(), name='delete_review'),
    path('reviews', ReviewDetails.as_view(), name='review-list'),
    path('get-airports/', views.get_airports, name='get_airports'),
    # path('airports/', views.airports, name='airports'),
    path('airports/', views.airports, name='airports'),

]
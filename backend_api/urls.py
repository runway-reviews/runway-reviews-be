from django.contrib import admin
from django.urls import path
from backend_api.views import UserDetails, ReviewDetails 

urlpatterns = [
    # path('', BookCreate.as_view()),
    # path('list/', BookList.as_view()),
    # path('<int:pk>', BookDetail.as_view()) 
    
    path('users/', UserDetails.as_view()),
    path('users/<int:user_id>/reviews/<int:review_id>/', ReviewDetails.as_view())
]
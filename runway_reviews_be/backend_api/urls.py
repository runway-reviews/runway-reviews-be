from django.urls import path
from backend_api.views import UserCreate, ReviewCreate, AirportIndex, AirportReviewsIndex 

urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:pk>', BookDetail.as_view()) 
]
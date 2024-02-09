from django.contrib import admin
from django.urls import path
from backend_api.views import UserDetails, ReviewDetails, ReviewList

urlpatterns = [
    # path('', BookCreate.as_view()),
    # path('list/', BookList.as_view()),
    # path('<int:pk>', BookDetail.as_view()) 
    # path('admin', admin.site.urls),
    path('user', UserDetails.as_view()),
    path('user/<int:user_id>/review/<int:review_id>', ReviewDetails.as_view()),
    path('reviews', ReviewList.as_view(), name='review-list'),
    path('user/<int:user_id>/review', ReviewDetails.as_view(), name='review-details')

]
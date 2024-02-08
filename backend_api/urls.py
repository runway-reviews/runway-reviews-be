from django.urls import path

from django.contrib import admin
from django.urls import path, include

from . import views  
urlpatterns = [
      # path('admin/', admin.site.urls),
      path('reviews/', views.reviews)
    # path('example/', views.example_view, name='example'), 
]

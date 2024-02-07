from django.urls import path

from django.contrib import admin
from django.urls import path, include

from . import views  
urlpatterns = [
      path('admin/', admin.site.urls)
    # path('example/', views.example_view, name='example'), 
]

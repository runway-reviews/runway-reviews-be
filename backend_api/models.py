from django.db import models

class User(models.Model): 
  username = models.CharField(max_length=100, unique=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=15)
  
  def __str__(self):
    return self.username
  
class Reviews(models.Model): 
  CATEGORY_TAGS = [
    ('Security', 'Security'),
    ('Restaurants', 'Restaurants'),
    ('Bathrooms', 'Bathrooms'),
    ('Arrivals/Departures', 'Arrivals/Departures'),
    ('Amenities', 'Amenities'),
    ('Accessibility', 'Accessibility')
  ]

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  airport = models.ForeignKey(Airport, on_delete=models.CASCADE) 
  comment = models.TextField(max_length=20)
  category = models.CharField(tags=CATEGORY_TAGS)
from django.db import models

class User(models.Model): 
  username = models.CharField(max_length=100, unique=True, null=False)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=15)

  def __str__(self):
    return self.username



class Airport(models.Model):
  name = models.CharField(max_length=55, null=True)

  def __str__(self):
    return self.name

class Review(models.Model): 
  CATEGORY_TAGS = [
    ('Security', 'Security'),
    ('Restaurants', 'Restaurants'),
    ('Bathrooms', 'Bathrooms'),
    ('General', 'General'),
    ('Amenities', 'Amenities'),
    ('Accessibility', 'Accessibility')
  ]
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True)
  comment = models.TextField(max_length=150)
  category = models.CharField(choices=CATEGORY_TAGS, max_length=50)

def __str__(self):
	return self.comment

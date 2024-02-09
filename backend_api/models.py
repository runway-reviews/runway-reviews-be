from django.db import models

class User(models.Model): 
  username = models.CharField(max_length=100, unique=True, null=False)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=15)
  date_created = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.username


class Review(models.Model): 
  CATEGORY_TAGS = [
    ('security', 'Security'),
    ('restaurants', 'Restaurants'),
    ('bathrooms', 'Bathrooms'),
    ('general', 'General'),
    ('amenities', 'Amenities'),
    ('accessibility', 'Accessibility')
  ]
  comment = models.TextField(max_length=150)
  category = models.CharField(choices=CATEGORY_TAGS)

  # user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
  # airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=False) 
  comment = models.TextField(max_length=150)
  category = models.CharField(choices=CATEGORY_TAGS)
  date_created = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.category

# Need to migrate into the db 
# class Airport(models.Model):
  # name = coming from an api call
  # id = how do we make these 
  
  # def __str__(self):
  #   return self.name 

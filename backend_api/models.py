from django.db import models

class User(models.Model): 
  username = models.CharField(max_length=100, unique=True, null=False)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=15)
  date_created = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.username

class Airport(models.Model):
  name = models.CharField(max_length=55, null=True)

  def __str__(self):
    return self.name

class Reviews(models.Model): 
  CATEGORY_TAGS = [
    ('security', 'Security'),
    ('restaurants', 'Restaurants'),
    ('bathrooms', 'Bathrooms'),
    ('general', 'General'),
    ('amenities', 'Amenities'),
    ('accessibility', 'Accessibility')
  ]
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  airport_id = models.CharField(max_length=9)
  comment = models.TextField(max_length=150)
  category = models.CharField(choices=CATEGORY_TAGS)
  # user = models.ForeignKey() # (User, on_delete=models.CASCADE)
  # airport = models.ForeignKey() #(Airport, on_delete=models.CASCADE) 

def __str__(self):
	return self.comment

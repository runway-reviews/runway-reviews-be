from django.db import models

class User(models.Model): 
  username = models.CharField(max_length=100, unique=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=15)
  
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

  # user = models.ForeignKey() # (User, on_delete=models.CASCADE)
  # airport = models.ForeignKey() #(Airport, on_delete=models.CASCADE) 

def __str__(self):
	return self.comment

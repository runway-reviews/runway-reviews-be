from rest_framework import serializers 
from .models import *
import pdb 

# Users
class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User  
        # fields = '__all__'
        fields = ['id', 'username', 'email', 'password', 'date_created', 'updated_at']

# Reviews 
class ReviewSerializer(serializers.ModelSerializer): 
    user_id = serializers.SerializerMethodField()
    # airport_id = serializers.SerializerMethodField()
    
    class Meta:
        model = Review  
        # fields = '__all__'
        fields = ['id', 'comment', 'category', 'date_created', 'updated_at', 'user_id'] # needs airport_id 
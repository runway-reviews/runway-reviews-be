from rest_framework import serializers 
from backend_api.models import User, Review, Airport
import pdb 

# User
class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User  
        # fields = '__all__'
        fields = ['id', 'username', 'email', 'password', 'date_created', 'updated_at']


# Review 
class ReviewSerializer(serializers.ModelSerializer): 
    user_id = serializers.SerializerMethodField()
    # airport_id = serializers.SerializerMethodField()

    class Meta:
        model = Review  
        # fields = '__all__'
        fields = ['id', 'comment', 'category', 'date_created', 'updated_at', 'user_id', 'airport_id'] # needs airport_id 


class AirportSerializer(serializers.ModelSerializer):
  attributes = serializers.SerializerMethodField()
  class Meta:
    model = Airport
    fields = ['id', 'attributes']

  def get_attributes(self, obj):
    return {
      'name': obj.name,
    }


class AirportSerializer(serializers.ModelSerializer):
  attributes = serializers.SerializerMethodField()
  class Meta:
    model = Airport
    fields = ['id', 'attributes']

  def get_attributes(self, obj):
    return {
      'name': obj.name,
    }
from rest_framework import serializers 
# from backend_api.models import User 
from backend_api.models import Airport 
# from django.forms import ValidationError

# class UserSerializer(serializers.ModelSerializer): 
#     description = serializers.SerializerMethodField()
#     class Meta:
#         model = User  
#         fields = '__all__'


class AirportSerializer(serializers.ModelSerializer):
  attributes = serializers.SerializerMethodField()
  class Meta:
    model = Airport
    fields = ['id', 'attributes']

  def get_attributes(self, obj):
    return {
      'name': obj.name,
    }
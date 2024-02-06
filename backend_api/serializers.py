from rest_framework import serializers 
from backend_api.models import User 
from django.forms import ValidationError

class UserSerializer(serializers.ModelSerializer): 
    description = serializers.SerializerMethodField()
    class Meta:
        model = User  
        fields = '__all__'

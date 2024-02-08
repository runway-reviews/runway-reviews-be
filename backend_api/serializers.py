from rest_framework import serializers 
from backend_api.models import User 
from backend_api.models import Review
from django.forms import ValidationError

class UserSerializer(serializers.ModelSerializer): 
    description = serializers.SerializerMethodField()
    class Meta:
        model = User  
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Review 
        fields = '__all__'

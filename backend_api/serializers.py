from rest_framework import serializers 
from backend_api.models import Airport, Review, User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
import pdb

class UserSerializer(serializers.ModelSerializer): 
    password_digest = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_digest']
       
    def get_password_digest(self, obj):
        return make_password(obj.password)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['password_digest'] = self.get_password_digest(instance)
        return {
            'id': str(instance.pk),
            'type': 'user',
            'attributes': representation
        }

class ReviewSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    airport_id = serializers.IntegerField(source='airport.id', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user_id', 'airport_id', 'comment', 'category']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation.get('id'),
            'type': 'review',
            'attributes': {
                'user_id': representation.get('user_id'),
                'airport_id': representation.get('airport_id'),
                'comment': representation.get('comment'),
                'category': representation.get('category'),
            },
            'relationships': {
                'user': {
                    'data': {
                        'id': representation.get('user_id'),
                        'type': 'user'
                    }
                }
            }
        }

    def save(self, **kwargs):
        user = kwargs.get('user', None)
        airport = kwargs.get('airport', None)
        self.validated_data['user'] = user
        self.validated_data['airport'] = airport
        return super().save(**kwargs)



class AirportSerializer(serializers.ModelSerializer):
  attributes = serializers.SerializerMethodField()
  class Meta:
    model = Airport
    fields = ['id', 'attributes']

    def validate_name(self, value):
        """
        Check that the name is indeed a string
        """
        if not isinstance(value, str):
            raise serializers.ValidationError("Name must be a string.")
        return value

    def to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        # Ensure instance.name is a string, even if it's originally bytes
        name = instance.name
        if isinstance(name, bytes):
            name = name.decode('utf-8')  # Decode bytes to string

        representation = super().to_representation(instance)
        representation['name'] = name  # Ensure 'name' in the output is always a string
        return {
            'id': str(instance.pk),
            'type': 'airport',
            'attributes': representation
        }
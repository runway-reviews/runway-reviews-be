from rest_framework import serializers 
from backend_api.models import User 
from backend_api.models import Review
from django.contrib.auth.hashers import make_password

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
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'airport_id', 'comment', 'category']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation.get('id'),
            'type': 'review',
            'attributes': {
                'user_id': representation.get('user').get('id'),
                'airport_id': representation.get('airport_id'),
                'comment': representation.get('comment'),
                'category': representation.get('category'),
            },
            'relationships': {
                'user': {
                    'data': {
                        'id': representation.get('user').get('id'),
                        'type': 'user'
                    }
                }
            }
        }

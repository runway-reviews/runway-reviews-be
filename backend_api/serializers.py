from rest_framework import serializers 
from backend_api.models import User 
from backend_api.models import Review
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
    attributes = serializers.SerializerMethodField()
    relationships = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'user_id', 'airport_id', 'comment', 'category', 'attributes', 'relationships']

    def get_attributes(self, obj):
        return {
            'user_id': obj.user.id,
            'airport_id': obj.airport_id,
            'comment': obj.comment,
            'category': obj.category
        }
    
    def get_relationships(self, obj):
        return {
            'user': {
                'data': {
                    'id': obj.user.id,
                    'type': 'user'
                }
            }
        }

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     return {
    #         'id': representation.get('id'),
    #         'type': 'review',
    #         'attributes': {
    #             'user_id': representation.get('user_id'),
    #             'airport_id': representation.get('airport_id'),
    #             'comment': representation.get('comment'),
    #             'category': representation.get('category'),
    #         },
    #         'relationships': {
    #             'user': {
    #                 'data': {
    #                     'id': representation.get('user_id'),
    #                     'type': 'user'
    #                 }
    #             }
    #         }
    #     }

    def save(self, **kwargs):
        user = kwargs.get('user')
        pdb.set_trace()
        user = User.objects.get(id=user.id)
        self.validated_data['user'] = user
        return super().save(**kwargs)
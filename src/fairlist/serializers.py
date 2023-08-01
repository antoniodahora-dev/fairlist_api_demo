from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Item


class UserRegistrationSerializer(BaseUserRegistrationSerializer):

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('email', 'username', 'password',)

class ItemSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Item
        fields = ['title', 'desc', 'priority', 'created_date', 'user',]
        
    def create(self, validated_data):
        return Item.objects.create(**validated_data)

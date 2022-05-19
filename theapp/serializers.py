from tkinter.tix import Tree
from rest_framework import serializers
from .models import Message
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }

class MessageSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False)

    class Meta:
        model = Message
        fields = ('id', 'message', 'created_at', 'updated_at', 'created_by')


    def validate_message(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("The message body is more than 250")


from rest_framework import status
from django.shortcuts import render
from rest_framework import permissions
from .serializers import MessageSerializer
from .models import Message
from rest_framework.views import APIView
from rest_framework.response import Response


class CreateMessage(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = MessageSerializer 

    def post(self, request):
        message_data = request.data
        if len(message_data['message'])>50:
                return Response("Words are more than 250")
        else:
            new_message = Message.objects.create(
                message = message_data["message"],
                created_by = request.user
            )

        serializer = MessageSerializer(new_message)
        new_message.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

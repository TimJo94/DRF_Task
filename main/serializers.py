from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=80, required=True)
    body = serializers.CharField(max_length=255)
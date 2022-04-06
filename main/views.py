from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import PostSerializer


class PostSerializerView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            Вы успешно создали пост!
            """
            return Response(message)

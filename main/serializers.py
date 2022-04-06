from rest_framework import serializers

from main.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        def create(self, validated_data):
            request = self.context.get('request')
            validated_data['author_id'] = request.user.id
            post = Post.objects.create(**validated_data)
            return post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'comment', 'image')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        comment = Comment.objects.create(**validated_data)
        return
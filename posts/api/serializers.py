from django.contrib.auth.models import User
from rest_framework import serializers
from posts.models import Post,Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ('user', 'content', 'created',)

class PostSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
          model = Post
          fields = ('url', 'title', 'user', 'created', 'comments' )

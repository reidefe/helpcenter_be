#from django.contrib.auth.models import User
from rest_framework import serializers
from ..models.models import Visitors, Article, Comment

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Visitors
        fields = ['name', 'email', 'password']

class RecursiveSerializer(serializers.Serializer):
    def to_representation(self,value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveSerializer(many=True, read_only = True)

    class Meta:
        model = Comment
        look_up_fields = 'slug'
        extra_kwargs = {
            'url': {'look_up_fields': 'slug'}
        }
        fields = ('post', 'name', 'body', 'parent', 'replies')


class ArticleSerializers(serializers.ModelSerializer):
    post_comment =  CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ['title', 'image', 'content',  'published', 'updated', 'slug', 'rating', 'post_comment' ]


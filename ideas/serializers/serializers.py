#from django.contrib.auth.models import User
from rest_framework import serializers
from ..models.model import Ideas, Comment


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
        fields = ('post',  'body', 'parent', 'replies')


class IdeaSerializers(serializers.ModelSerializer):
    idea_comments =  CommentSerializer(many=True)

    class Meta:
        model = Ideas
        fields = ['title', 'images', 'content',  'published', 'updated' ,'slug', 'rating', 'idea_comments' ]


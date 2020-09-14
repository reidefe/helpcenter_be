#from django.contrib.auth.models import User
from rest_framework import serializers
from ..models.model import Guides




class GuidesSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Guides
        fields = ['title', 'images', 'content',  'published', 'slug', 'likes' ]


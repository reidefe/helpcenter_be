from django.shortcuts import render

from .models.model import Ideas, Comment
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers.serializers import IdeaSerializers, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework import status

#simple Viewset for Ideas
class IdeasView(ModelViewSet ):
    queryset = Ideas.objects.all()
    serializer_class = IdeaSerializers

    #custom method to get the most liked/supported ideas from all ideas
    @action(detail=False)
    def Most_liked_ideas(self, request):
        ideas = Ideas.objects.latest()
        serializer = self.get_serializer(ideas)
        return Response (serializer.data)


#Viewset for Comments
class CommentsViews(ModelViewSet):
    queryset = Comment.objects.all
    serializer_class = CommentSerializer
   
    
    
    #list route for displaying root nodes of each comment section
    @action(detail=False)
    def list(self, request):
        queryset = Comment.objects.filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


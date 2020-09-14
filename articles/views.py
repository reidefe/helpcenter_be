from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .models.models import Visitors, Comment, Article
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers.serializers import UserSerializers, ArticleSerializers, CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework import status
 
# Generic views for Article operations
class ArticleCreate(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = 'slug'

class ArcticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = 'slug'

class ArticleDelete(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = 'slug'

class ArticleUpdate(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    lookup_field = 'slug'


# Viewset for Comments
class CommentsViews(ModelViewSet):
    queryset = Comment.objects.all
    serializer_class = CommentSerializer
   
    """ HAD PROBLEMS WITH THIS SETS OF METHOD, PLEASE BARE WITH ME AS I WOULD HAVE IT FIXED 
    # method to create comment
    def create(self, request):
       comment = self.create(request) 
       serializer = self.get_serializer(data=request.data)
       return Response(serializer.data)
    
    # method to delete comments
    def update(self, request):
     
    #method
    def destroy(self, request):
    queryset = Comment.objects.delete(pk=request.pk)
    return Response (status.HTTP_202_ACCEPTED)
    """
    
    #list route for displaying root nodes of each comment section
    @action(detail=False)
    def list(self, request):
        queryset = Comment.objects.filter(parent=None)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


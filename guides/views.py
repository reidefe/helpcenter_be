

from .models.model import Guides
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers.serializer import GuidesSerializers
from rest_framework.decorators import action
from rest_framework.response import Response 
from rest_framework import status

#simple Viewset for Ideas
class IdeasView(ModelViewSet ):
    queryset = Guides.objects.all()
    serializer_class = GuidesSerializers
    

    #custom method to get the most liked/supported guides from all ideas
    @action(detail=False)
    def Most_helpful_guide(self, request):
        ideas = Guides.objects.latest()
        serializer = self.get_serializer(ideas)
        return Response (serializer.data)



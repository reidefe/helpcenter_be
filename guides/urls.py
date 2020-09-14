from rest_framework.routers import DefaultRouter
from .views import  GuidesSerializers
from django.urls import path, include




router = DefaultRouter()

router.register(r'guides', GuidesSerializers, basename='guides')


urlpatterns = [
    path('', include(router.urls) )
]
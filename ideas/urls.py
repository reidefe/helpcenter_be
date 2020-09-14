from rest_framework.routers import DefaultRouter
from .views import CommentsViews, IdeasView
from django.urls import path, include

router = DefaultRouter()

router.register(r'Ideas', IdeasView , basename='Ideas')
router.register(r'comments', CommentsViews , basename='Comments')




urlpatterns = [
    path('^IdeasApi', include(router.urls) )
]
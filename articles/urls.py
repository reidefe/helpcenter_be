from rest_framework import routers
from views import ArcticleList, ArcticleList,ArticleCreate, ArticleDelete, CommentsViews

from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r'^article', CommentsViews)

urlpatterns = [
    path(r'^comments/', CommentsViews.as_view()),
]

urlpatterns += router.urls

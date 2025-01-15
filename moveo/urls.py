from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CodeblockViewSet
from . import views

# This router handles the routing for the CodeblockViewSet, 
# allowing CRUD operations on the 'codeblocks' endpoint.
router = DefaultRouter()
router.register(r'codeblocks', CodeblockViewSet, basename='codeblock')

urlpatterns = [
    # This includes all routes registered with the DefaultRouter.
    # DefaultRouter automatically generates routes for the 
    # CodeblockViewSet, such as list, create, retrieve, update, and delete.
    path('', include(router.urls)),

    # Endpoint: '/index/'
    # This route is mapped to the 'index' view. 
    # It serves as a basic test or health check endpoint.
    path('index/', views.index),

    # Endpoint: '/test/'
    # This route is mapped to the 'test' view. 
    # It serves as another simple endpoint for testing purposes.
    path('test/', views.test),
]

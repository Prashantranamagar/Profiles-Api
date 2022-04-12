from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets 
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from . import  models
from . import permissions

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview =[
            'Uses HTTP methods as function {get, post, patch, put, delete}',
            'Is similar to a traditonal Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',

        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                    serializer.errors,
                    status = status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handel updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API View"""
    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """return a hello message"""

        a_viewset = [
            'User actions (list, create, retrive, update, partial_update)', 
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',

        ]
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid|():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST

            )

    def retrive(self, request, pk=None):
        """Handele getting an object by its ID"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating parts of an object"""
        return Response({'http_methood':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_methood':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = {'name', 'email',}


class UserLoginApiView(ObtainAuthToken):
    """Handel creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
        
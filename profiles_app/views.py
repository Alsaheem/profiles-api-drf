from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import HelloSerializer,UserProfileSerializer,ProfileFeedSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateOwnProfile,PostOwnStatus
from .models import UserProfile,ProfileFeed
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class HelloView(APIView):
    serializer_class = HelloSerializer

    def get(self,request,format=None):
        an_api_view = [
            'this is my first api',
            'this is the second line',
            'three of faces',
            'four of hearts'
        ]
        return Response({'message':'Hello','an_api_view':an_api_view})

    def post(self,request):
        serializer = HelloSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.data.get('first_name')
            last_name = serializer.data.get('last_name')
            message = "Hello , Mr {0}-{1}".format(first_name,last_name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """handles updating an object"""
        # logic
        return Response({'message':'this method is used for put'})

    def patch(self,request,pk=None):
        """handles patching part of an an object"""
        # logic
        return Response({'message':'this method is used for patch'})

    def delete(self,request,pk=None):
        """handles deleting an object"""
        # logic
        return Response({'message':'this method is used for delete'})


class HelloViewset(viewsets.ViewSet):
    '''test api viewset'''
    serializer_class = HelloSerializer

    def list(self,request):
        a_viewset = [
            'uses actions (list,create,update,put,patch,delete)',
            'Automatically maps the urls with routers',
            'more functionality with less code'
        ]
        return Response({'message':'hello','a_viewset':a_viewset})
    
    def create(self,request):
        serializer = HelloSerializer(data=request.data)
        if serializer.is_valid():
            first_name = serializer.data.get('first_name')
            last_name = serializer.data.get('last_name')
            message = "Hello , Mr {0}-{1}".format(first_name,last_name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        """handles updating an object"""
        # logic
        return Response({'message':'this method is used for GET - retrieving'})

    def update(self,request,pk=None):
        """handles patching part of an an object"""
        # logic
        return Response({'message':'this method is used for PUT - update'})

    def partial_update(self,request,pk=None):
        """handles deleting an object"""
        # logic
        return Response({'message':'this method is used for PATCH - partial_update'})

    
    def destroy(self,request,pk=None):
        """handles patching part of an an object"""
        # logic
        return Response({'message':'this method is used for DELETE - delete'})

class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name','first_name','email',)

class LoginViewset(viewsets.ViewSet):
    # checks the email and password , then returns an authtoken
    serializer_class=AuthTokenSerializer

    def create(self,request):
        # use authtoken an_api_view to validate the request
        return ObtainAuthToken().post(request)

        # "token": "c22ec2fa1cdcd02afd86186c93ee9e125114c29d"

class ProfileFeedViewset(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedSerializer
    queryset = ProfileFeed.objects.all()
    permission_classes = (PostOwnStatus,IsAuthenticated)

    def perform_create(self,serializer):
        serializer.save(user_profile = self.request.user)



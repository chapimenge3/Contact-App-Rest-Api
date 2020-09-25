# Django build in library imports 
from django.shortcuts import render

# My Application imports
from authentication.models import User 
from authentication.serializers import UserSerializer
from Contact.permission import IsOwnerOrReadOnly

# Restframework imports 
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions

class UserSignUpViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    UserSignUpViewset is used for signup purpuse it only create user instance 
    it can't retrive , update and delete user object 
    '''
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileViewset(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    '''
    UserProfileViewset is for profile for user (only for request.user ) . it can used for retrieve , update and delete
    '''
    serializer_class = UserSerializer
    queryset = None
    permission_classes = [ permissions.IsAuthenticated, IsOwnerOrReadOnly ] 
    
    def get_queryset(self):
        return User.objects.get(username=self.request.user.username)
    
    

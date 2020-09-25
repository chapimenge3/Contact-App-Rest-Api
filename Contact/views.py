from django.shortcuts import render


from Contact.serializers import ContactSerializer
from Contact.models import Contact
from Contact.permission import IsOwnerOrReadOnly

# Restframework imports 
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

class ContactViewSet(viewsets.ModelViewSet):
    '''
    Contact Viewset is for Creating, updating , retrieving and deleting contact 
    '''
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [ IsOwnerOrReadOnly, permissions.IsAuthenticated ]

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
    
    def create(self, request, *args, **kwargs):
        '''
        it is called when we send post data to our api
        '''
        error = None
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        error = self.perform_create(serializer) # used for controling annoymous user to be added in contact.owner
        headers = self.get_success_headers(serializer.data)
        if not error: # if error return not none it is fine and authorized it  authorized it 
            return Response(status=error, headers=headers)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers) 
    
    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
            return None
        except Exception as e:
            return status.HTTP_401_UNAUTHORIZED
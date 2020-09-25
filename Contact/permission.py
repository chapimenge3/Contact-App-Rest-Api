from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    
    Custom permission to only the owner of the contact to edit and delete 

    '''
    
    def has_object_permission(self, request, view, obj):
        # Read permission are allowed to any request  
        if request.method and obj.owner == request.user :
            return obj.owner == request.user
        return False 

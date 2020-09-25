# Django Built-in Imports
from django.urls import  path, include

# My Application imports
from authentication.views import  UserSignUpViewset , UserProfileViewset 

# Restframwork import 
from rest_framework.routers import DefaultRouter

# Router Class for automatic url for my viewsets in views.py
router = DefaultRouter()

router.register(r'signup', UserSignUpViewset, basename="Signup") # registering the viewset for User for signup only
router.register(r'user', UserProfileViewset, basename="User") # Registering the viewset for the user update, retrieve and deleting

urlpatterns = [
    path('', include(router.urls)),   
]

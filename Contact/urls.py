from django.urls import path, include

from Contact.views import ContactViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contact', ContactViewSet) # registering the viewset for Conatct

urlpatterns = [
    path('', include(router.urls)), 
]

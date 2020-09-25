from rest_framework import serializers

from authentication.models import User

class UserSerializer(serializers.ModelSerializer):
    '''
    Serializer Class for User Model that can serialize important field choosen using in the Meta class field attribute
    '''
    date_joine = serializers.ReadOnlyField(source='date_joined')
    class Meta:
        model = User
        exclude = ['is_staff', 'is_active', 'password', 'last_login' ,'is_superuser', 'user_permissions', 'groups']
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'
        
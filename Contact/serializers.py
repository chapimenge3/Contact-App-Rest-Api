from rest_framework import serializers

from Contact.models import  Contact


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # Note = serializers.CharField(style={'base_template': 'textarea.html'}, blank=True)
    class Meta:
        model = Contact
        fields= ['owner', 'first_name', 'last_name', 'phone', 'email', 'date_of_birth', 
                 'address', 'campany', 'social_medias',  'image']
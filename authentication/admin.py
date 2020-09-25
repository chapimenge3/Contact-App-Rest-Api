# Django built-in imports
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms

# My applications import
from authentication.models import User


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label='old Pass')
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email','first_name', 'last_name', 'phone', 'profile', 
                   'date_of_birth', 'address', 'campany', 'social_medias', 'is_staff', 'last_login', 
                   'is_superuser', 'user_permissions', 'groups']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]        

class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    list_display = ('username', 'email')
admin.site.register( User, UserAdmin )
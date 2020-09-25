from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    '''
    User Model that extends Abstract user and add some extra field (phone , profile , birth_date and Social Medias )
    Social Media is another Django Model 
    '''

    phone = models.CharField(_('Phone Number'), unique=True, max_length=20)
    date_of_birth = models.DateField(_("Date of Birth"), blank=True, null=True)
    profile = models.ImageField(upload_to="media/userProfile", max_length=100, blank=True, null=True)
    address = models.ForeignKey("Address", verbose_name=_("UserAddress"), on_delete=models.CASCADE, blank=True, null=True)
    campany = models.ForeignKey("Campany", verbose_name=_("UserCampany"), on_delete=models.CASCADE, blank=True, null=True)
    social_medias = models.ManyToManyField("SocialMedia", blank=True)

    def __str__(self):
        '''
        it return when we want to print out the object
        '''
        
        return self.first_name


class Campany(models.Model):
    '''
    Campany is used to represent the campany name , title and website url 
    '''

    name = models.CharField(_("Name"), max_length=50)
    title = models.CharField(_("Title"), max_length=50)
    website = models.URLField(_("Website"), max_length=200)

    def __str__(self):
        '''
        it return when we want to print out the object
        '''

        return self.name

class Address(models.Model):
    '''
    Address is used to represent formal address of the user or the contact 
    '''

    country = models.CharField(_("Country"), max_length = 30, )
    state = models.CharField(_("State"), max_length = 30, blank=True, null=True)
    city = models.CharField(_("City"), max_length = 30, blank=True, null=True)
    street = models.CharField(_("Street"), max_length = 30, blank=True, null=True)
    po_box = models.CharField(_("PO Box"), max_length = 30, blank=True, null=True)
    zip_code = models.CharField(_("Zip code"), max_length = 30, blank=True, null=True)
    home_number = models.CharField(_("Home Number"), max_length = 30, blank=True, null=True)


    def __str__(self):
        '''
        it return when we want to print out the object
        '''
        return self.country

class SocialMedia(models.Model):
    '''
    Social Medial used for representing the Any Social medias profile   
    '''

    name = models.CharField(_("Social Media Name"), max_length=50)
    website = models.CharField(_("website"), max_length=50)
    logo = models.ImageField(upload_to ="media\Social Meida Logo") 

    def __str__(self):
        return self.name

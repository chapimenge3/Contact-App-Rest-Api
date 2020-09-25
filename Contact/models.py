from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    '''
    it is Django Model . Contact have various field for saving contacts in database
    '''

    owner = models.ForeignKey('authentication.User', verbose_name=_("owner"), on_delete=models.CASCADE)
    first_name = models.CharField(_("First Name"), max_length=50 )
    last_name = models.CharField(_("Last Name"), max_length=50, blank=True, default="" )
    phone = models.CharField(_('Phone Number'), max_length=20)
    email = models.EmailField(_('email address'), blank=True, null=True)
    date_of_birth = models.DateField(_("Date of Birth"), blank=True, null=True)
    campany = models.ForeignKey("authentication.Campany", on_delete=models.CASCADE, blank=True, null=True)
    address = models.ForeignKey("authentication.Address", verbose_name=_("Address"), on_delete=models.CASCADE, blank=True, null=True)
    website = models.URLField(_("Website"), max_length=200, blank=True, null=True)
    social_medias = models.ManyToManyField("authentication.SocialMedia", verbose_name=_("Social Medias"), blank=True)
    Note = models.TextField(blank=True, null=True),
    image = models.ImageField(_("Image"), upload_to="media\contactImage", max_length=None, blank=True, null=True)
    
    def __str__(self):
        '''
        it return when we want to print out the object
        '''

        return self.first_name

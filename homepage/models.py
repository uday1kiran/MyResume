from django.db import models
from phone_field import PhoneField
#pip install django-phone-field
#https://pypi.org/project/django-phone-field/

# Create your models here.
class Profile(models.Model):
    dateofbirth = models.DateTimeField(null=True, blank=True)
    website = models.TextField(blank=True)
    degree = models.TextField(blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.TextField(blank=True)
    city = models.TextField(blank=True)
    freelance = models.BooleanField(default=False)
	
    heading = models.TextField(blank=True)
    caption = models.TextField(blank=True)
    summary = models.TextField(blank=True)
	
    profile_captions_csv = models.TextField(blank=True)
    name = models.TextField(blank=True)
    webtitle = models.TextField(blank=True)

    def __str__(self):
        return self.heading


class Skill(models.Model):
    name = models.TextField(blank=True)
    progress = models.SmallIntegerField(default=10)
	
    def __str__(self):
        return self.name
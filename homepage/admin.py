from django.contrib import admin
from phone_field import PhoneField
from .models import Profile,Skill
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    pass
	

admin.site.register(Skill)
admin.site.register(Profile)


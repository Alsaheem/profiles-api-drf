from django.contrib import admin
from .models import UserProfile,ProfileFeed
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(ProfileFeed)
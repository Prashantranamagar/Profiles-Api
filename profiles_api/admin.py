from django.contrib import admin
from .models import UserProfileManager
from .models import UserProfile
from .models import ProfileFeedItem

admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)

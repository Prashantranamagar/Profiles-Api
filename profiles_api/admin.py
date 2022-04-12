from django.contrib import admin
from .models import UserProfileManager
from .models import UserProfile


admin.site.register(UserProfile)
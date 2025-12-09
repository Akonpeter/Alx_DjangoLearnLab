from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (('profile Info',{'fields': ('bio', 'profile_picture', 'followers')}),
                                       
                                       )
admin.site.register(CustomUser, CustomUserAdmin)

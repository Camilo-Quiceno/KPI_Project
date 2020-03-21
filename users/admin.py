"""User admin classes."""

#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

#Models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)
class ProfileAdmgin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('user','trained_in',)
    list_editable = ('trained_in',)
    search_fields = ('user__username','user__email','user__first_name','user__last_name')

    list_filter = ('trained_in',)


#Extending the existing User model

class ProfileInLine(admin.StackedInline):
    """Profile in-line admin for users."""
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInLine,)
    

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

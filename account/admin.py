from django.contrib import admin
from .models import CustomUser, Profile


# Register your models here.
@admin.register(CustomUser)
class Custom_user_admin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class Profile_admin(admin.ModelAdmin):
    pass

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
UserAdmin.list_display+=('info',)
UserAdmin.fieldsets+=(
    (
        'User_info',{
            'fields':('info', )
        }
    ),

)
admin.site.register(User,UserAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Contact
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role','is_active', 
                    'is_staff', 'is_superuser', 'last_login',)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "role", "password1", "password2", "profile_pic"),
            },
        ),
    )
   
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Contact, ContactAdmin)
    
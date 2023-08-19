
from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Customize the admin display fields and other settings if needed
    list_display = ['id','email', 'username', 'first_name','last_name','phone_number',]
    list_filter = []
    filter_horizontal = ()
    search_fields = ['email', 'username', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_driver')}),
    )

admin.site.register(User, CustomUserAdmin)

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Sign

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'birth_date')
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Pessoais', {'fields': ('birth_date', 'birth_time', 'birth_city')}),
    )

@admin.register(Sign)
class SignAdmin(admin.ModelAdmin):
    list_display = ('name', 'element', 'symbol')

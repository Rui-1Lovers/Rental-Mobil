from django.contrib import admin
from .models import User, Car, Customer, Rental
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('no_hp', 'alamat')}),
    )

admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Rental)
# Register your models here.

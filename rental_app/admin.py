from django.contrib import admin
from .models import User, Car, Customer, Rental
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Extend admin user untuk menambahkan no_hp dan alamat
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('no_hp', 'alamat')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'no_hp')

# Admin Mobil
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('plat_nomor', 'merk', 'model', 'harga_per_hari', 'tersedia')
    list_filter = ('tersedia', 'merk')
    search_fields = ('plat_nomor', 'merk', 'model')

# Admin Customer
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'no_telepon', 'user')
    search_fields = ('nama', 'email')

# Admin Rental
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('car', 'customer', 'tanggal_mulai', 'tanggal_selesai', 'total_harga', 'status', 'admin')
    list_filter = ('status', 'tanggal_mulai', 'tanggal_selesai')
    search_fields = ('car__plat_nomor', 'customer__nama', 'admin__username')

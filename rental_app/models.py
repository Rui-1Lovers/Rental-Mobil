from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User
class User(AbstractUser):
    no_hp = models.CharField(max_length=20, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

# Mobil
class Car(models.Model):
    plat_nomor = models.CharField(max_length=20)
    merk = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    harga_per_hari = models.DecimalField(max_digits=10, decimal_places=2)
    tersedia = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.plat_nomor} - {self.merk} {self.model}"

# Pelanggan
class Customer(models.Model):
    # Ganti OneToOne → ForeignKey agar satu user bisa punya banyak customer
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers')
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    no_telepon = models.CharField(max_length=15)

    def __str__(self):
        return self.nama

# Penyewaan
class Rental(models.Model):
    STATUS_CHOICES = [
        ('proses', 'Proses'),
        ('selesai', 'Selesai')
    ]
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    total_harga = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='proses')

    # Admin = user yang menangani rental
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rental_dikelola')

    def __str__(self):
        return f"Sewa {self.car} oleh {self.customer} ({self.status})"

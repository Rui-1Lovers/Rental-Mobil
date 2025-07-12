from rest_framework import serializers
from rental_app.models import Car, Customer, Rental, User
from django.contrib.auth import get_user_model

# Serializer untuk User (Admin & Customer)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'no_hp', 'alamat']

# Mobil
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

# Customer (user dipilih dari daftar user yang sudah ada, bukan dibuat baru)
class CustomerSerializer(serializers.ModelSerializer):
    # Hanya bisa memilih dari user yang sudah ada, bisa disesuaikan filter-nya jika hanya admin
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Customer
        fields = '__all__'

# Rental
class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

    def create(self, validated_data):
        car = validated_data['car']
        durasi = (validated_data['tanggal_selesai'] - validated_data['tanggal_mulai']).days
        validated_data['total_harga'] = durasi * car.harga_per_hari

        # Isi admin otomatis dari user yang sedang login
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            validated_data['admin'] = request.user

        return super().create(validated_data)

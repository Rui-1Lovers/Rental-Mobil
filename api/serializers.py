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

# Customer (user otomatis = request.user)
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'nama', 'email', 'no_telepon']  # user tidak perlu diinput manual

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request and request.user.is_authenticated else None
        return Customer.objects.create(user=user, **validated_data)

# Rental
class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

    def create(self, validated_data):
        car = validated_data['car']
        durasi = (validated_data['tanggal_selesai'] - validated_data['tanggal_mulai']).days
        validated_data['total_harga'] = durasi * car.harga_per_hari

        request = self.context.get('request')
        if request and hasattr(request, "user"):
            validated_data['admin'] = request.user

        return super().create(validated_data)

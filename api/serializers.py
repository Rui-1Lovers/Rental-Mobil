from rest_framework import serializers
from rental_app.models import Car, Customer, Rental, User
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'no_hp', 'alamat']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = get_user_model().objects.create(**user_data)
        customer = Customer.objects.create(user=user, **validated_data)
        return customer

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

    def create(self, validated_data):
        car = validated_data['car']
        durasi = (validated_data['tanggal_selesai'] - validated_data['tanggal_mulai']).days
        validated_data['total_harga'] = durasi * car.harga_per_hari
        return super().create(validated_data)
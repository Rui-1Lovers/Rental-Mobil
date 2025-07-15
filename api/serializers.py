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
    class Meta:
        model = Customer
        fields = ['id', 'nama', 'email', 'no_telepon']

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request and request.user.is_authenticated else None

        if user is None:
            
            from django.contrib.auth import get_user_model
            User = get_user_model()
            user = User.objects.first()

        return Customer.objects.create(user=user, **validated_data)

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'
        read_only_fields = ['total_harga']  # ⛔ Jangan izinkan input total_harga

    def create(self, validated_data):
        car = validated_data['car']
        durasi = (validated_data['tanggal_selesai'] - validated_data['tanggal_mulai']).days
        validated_data['total_harga'] = durasi * car.harga_per_hari

        request = self.context.get('request')
        user = request.user if request and hasattr(request, 'user') and request.user.is_authenticated else None
        if not user:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            user = User.objects.first()
        validated_data['admin'] = user
        return super().create(validated_data)

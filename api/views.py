from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rental_app.models import Car, Customer, Rental, User
from api.serializers import CarSerializer, CustomerSerializer, RentalSerializer, UserSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        # Kirim request ke serializer agar bisa ambil request.user sebagai user di Customer
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_queryset(self):
        # Boleh akses hanya customer miliknya sendiri (opsional, bisa hapus jika semua boleh lihat)
        user = self.request.user
        return Customer.objects.filter(user=user)

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        # Kirim request ke serializer agar bisa ambil request.user sebagai admin
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_queryset(self):
        # Boleh akses hanya rental yang dikelola oleh admin ini (opsional)
        user = self.request.user
        return Rental.objects.filter(admin=user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

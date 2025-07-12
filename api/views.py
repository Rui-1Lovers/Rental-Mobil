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
    permission_classes = [IsAuthenticated]  # agar hanya user login yang bisa akses (opsional)

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        """Kirim request ke serializer agar bisa ambil request.user sebagai admin"""
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

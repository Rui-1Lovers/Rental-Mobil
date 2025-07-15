from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rental_app.models import Car, Customer, Rental, User
from api.serializers import CarSerializer, CustomerSerializer, RentalSerializer, UserSerializer
from rest_framework.permissions import AllowAny


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Customer.objects.filter(user=user)
        return Customer.objects.all()  # ✅ anonymous user lihat semua

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [AllowAny]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_queryset(self):
        return Rental.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

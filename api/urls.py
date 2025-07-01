from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register(r'cars', views.CarViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'rentals', views.RentalViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

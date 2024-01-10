from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import BookingViewSet, MenuViewSet, index

router = SimpleRouter(trailing_slash=False)
router.register('booking/tables', BookingViewSet, basename='booking')
router.register('menu', MenuViewSet, basename='menu')

urlpatterns = [
    path('api-token-auth', obtain_auth_token),
    path('', index)
] + router.urls
from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import views, viewsets
from rest_framework.response import Response

from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

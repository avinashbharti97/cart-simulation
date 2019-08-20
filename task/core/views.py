from django.shortcuts import render, get_object_or_404
from .models import Cart, Product
from .cart_api import CartSerializer, ProductSerializer
from rest_framework import generics

# Create your views here.

class GetCart(generics.ListAPIView):
    serializer_class = CartSerializer

    def get_queryset(self):
        id = self.kwargs['user_id']
        return Cart.objects.filter(userId = id)


def index(request):
    return render(request, 'index.html')
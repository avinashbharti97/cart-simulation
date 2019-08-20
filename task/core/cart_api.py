from rest_framework import serializers, viewsets
from django.conf import settings
from django.contrib.auth.models import User
from rest_auth.serializers import UserDetailsSerializer
from rest_framework import generics
from .models import Product, Cart

app_name = 'api'

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'stock', 'timeOfcreation')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
    class Meta:
        model = User
        fields = ('id', 'username')



class CartSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cart
        fields = ('id', 'productId', 'userId', 'timeOfAllocation', 'noOfItemsOrdered')
        # fields = ('id', 'productId','timeOfAllocation', 'noOfItemsOrdered')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# class GetTaskViewSet(viewsets.ModelViewSet):
#     # queryset = AllocateTask.objects.filter(workerId)
#     serializer_class = AllocateTaskSerializer

#     def get_queryset(self):
  
       
#         return AllocateTask.objects.filter(workerId)
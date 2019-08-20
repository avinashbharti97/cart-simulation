from rest_framework import serializers, viewsets
from rest_framework import generics
from .models import Product, User, Cart

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'stock', 'timeOfcreation')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'description')



class CartSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cart
        fields = ('id', 'productId', 'userId', 'timeOfAllocation', 'noOfItemsOrdered')


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
from rest_framework import serializers
from customer.models import Customer
from cart.models import Cart 
from delivery.models import Vendor
from inventory.models import Product
from cart.models import Cart 
from delivery.models import Vendor
from inventory.models import Product
from order.models import Order
from payment.models import Payment
from vendor.models import Vendor

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    products =ProductSerializer(many = True)
    class Meta:
        model = Cart
        fields = "__all__"
        
class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields= "__all__"
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = "__all__"
                
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model =Order
        fields ="__all__"
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Payment
        fields = "__all__"
            
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields="__all__"
        